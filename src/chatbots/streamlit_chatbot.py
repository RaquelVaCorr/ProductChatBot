import streamlit as st
from streamlit_chat import message
import os
from dotenv import load_dotenv
load_dotenv()
import os
from langchain.chat_models import ChatOpenAI
from utils.helpers import get_initial_message, load_data, initialize_pinecone, create_embeddings, augment_prompt, create_vectorstore
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
# Load data
path_products_json = '.\datasources\json\productos.json'
data = load_data(path_products_json)

path_api_keys_json = '.\datasources\json\keys.json'
api_keys = load_data(path_api_keys_json)

# Initialize Pinecone and OPENAI instances
pc_api_key = api_keys['PC_API_KEY']
openai_api_key = api_keys['OPENAI_API_KEY']
pc, index = initialize_pinecone(pc_api_key)
# Setup chat model
chat = ChatOpenAI(
    openai_api_key=openai_api_key,
    model='gpt-3.5-turbo'
)

# Setup embedding model
from langchain.embeddings.openai import OpenAIEmbeddings
embed_model = OpenAIEmbeddings(model="text-embedding-ada-002")

# Create embeddings
create_embeddings(data, embed_model, index)



# Create vectorstore
vectorstore = create_vectorstore(index, embed_model)


st.title("Bruno Child Offers Chatbot")
st.subheader("Asistente AI:")



if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []

query = st.text_input("Pregunta: ", key="input")

if 'messages' not in st.session_state:
    st.session_state['messages'] = get_initial_message()


if query:
    with st.spinner("generating..."):

        messages = st.session_state['messages']

                # create a new user prompt
        prompt = HumanMessage(
            content=augment_prompt(query, vectorstore)
        )
        # add to messages
        messages.append(prompt)

        res = chat(messages)

        messages.append(AIMessage(content= res.content))
        st.session_state.past.append(query)
        st.session_state.generated.append(res.content)

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

    with st.expander("Show Messages"):
        st.write(messages)





