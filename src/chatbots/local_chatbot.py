import os
from langchain.chat_models import ChatOpenAI
from src.utils.helpers import load_data, initialize_pinecone, create_embeddings, augment_prompt, create_vectorstore
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

# Load data
data = load_data()
print(data)

# Initialize Pinecone
# Load data
path_products_json = '.\datasources\json\productos.json'
data = load_data(path_products_json)

path_api_keys_json = '.\datasources\json\keys.json'
api_keys = load_data(path_api_keys_json)

# Setup embedding model
from langchain.embeddings.openai import OpenAIEmbeddings
embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# Create embeddings
create_embeddings(data, embed_model, index)

# Setup chat model
chat = ChatOpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo'
)

# Create vectorstore
vectorstore = create_vectorstore(index, embed_model)

# Define and run queries
queries = [
    '¿Qué geles tienes?',
    '¿Sabes sobre la historia de Colombia?',
    '¿Quién escribió el libro "El túnel"?',
    '¿Qué productos tienes para el cabello?'
]

for query in queries:
    prompt = augment_prompt(query, vectorstore)
    res = chat([HumanMessage(content=prompt)])
    print('\n')
    print("*"*50)
    print('\n')
    print(query)
    print('\n')
    print(res.content)
