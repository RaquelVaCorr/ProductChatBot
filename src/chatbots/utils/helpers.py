import json
import time
from pinecone import Pinecone, ServerlessSpec
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone as LangchainPinecone
from tqdm.auto import tqdm
from langchain.schema import SystemMessage, HumanMessage, AIMessage

def load_data(filename='datasources\json\productos.json'):
    """
    Load data from a JSON file.

    Args:
        filename (str): Name of the JSON file containing the data. Default is 'datasources\json\productos.json'.

    Returns:
        list: List of data loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        loaded_list = json.load(file)
    return loaded_list

def initialize_pinecone(api_key, index_name='llama-2-rag'):
    """
    Initialize Pinecone with the API key and create an index if it doesn't exist.

    Args:
        api_key (str): API key to authenticate with Pinecone.
        index_name (str): Name of the index in Pinecone. Default is 'llama-2-rag'.

    Returns:
        tuple: Pinecone object and the created or existing index.
    """
    pc = Pinecone(api_key=api_key)
    spec = ServerlessSpec(cloud="aws", region="us-east-1")

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
    if index_name not in existing_indexes:
        pc.create_index(index_name, dimension=1536, metric='dotproduct', spec=spec)
        while not pc.describe_index(index_name).status['ready']:
            time.sleep(1)

    index = pc.Index(index_name)
    time.sleep(1)  # Short delay to ensure the index is ready
    index.describe_index_stats()
    return pc, index

def create_embeddings(data, embed_model, index, batch_size=100):
    """
    Create and upload embeddings to a Pinecone index in batches.

    Args:
        data (list): List of data to create embeddings for.
        embed_model (EmbeddingModel): Embedding model used to generate embeddings.
        index (Pinecone.Index): Pinecone index where the embeddings will be stored.
        batch_size (int): Batch size for processing the data. Default is 100.

    Returns:
        None
    """
    for i in tqdm(range(0, len(data), batch_size)):
        i_end = min(len(data), i + batch_size)
        batch = data[i:i_end]
        ids = list(range(i, i_end))
        ids_str = [str(id) for id in ids]
        embeds = embed_model.embed_documents(batch)
        metadata = [{'text': x} for x in batch]
        index.upsert(vectors=zip(ids_str, embeds, metadata))

def augment_prompt(query, vectorstore):
    """
    Augment a query using similar information found in a vectorstore.

    Args:
        query (str): Query for which to generate the augmented prompt.
        vectorstore (LangchainPinecone): Vectorstore object for performing similarity search.

    Returns:
        str: Augmented prompt with additional context information.
    """
    results = vectorstore.similarity_search(query, k=5)
    source_knowledge = "\n".join([x.page_content for x in results])
    augmented_prompt = f"""
    Using the contexts below, answer the query. All questions should be about products, prices, and discounts in the context, or personal care and bathroom products.

    Contexts:
    {source_knowledge}

    Query: {query}
    """
    return augmented_prompt

def create_vectorstore(index, embed_model):
    """
    Create a vectorstore using Pinecone and an embedding model.

    Args:
        index (Pinecone.Index): Pinecone index to store vectors.
        embed_model (EmbeddingModel): Embedding model to generate query vectors.

    Returns:
        LangchainPinecone: Created vectorstore object.
    """
    text_field = "text"
    return LangchainPinecone(index, embed_model.embed_query, text_field)


def get_initial_message():
    messages = [
        SystemMessage(content="You are a helpful assistant."),
        AIMessage(content="Hola soy tu asistente virtual para 'Bruno Store' ¿Cómo puedo ayudarte hoy?")  
    ]
    return messages

