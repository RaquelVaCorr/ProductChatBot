import os
from langchain.chat_models import ChatOpenAI
from pdfquery import PDFQuery

from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

#PDF extraction
pdf = PDFQuery('Bruno_child_offers.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]
prodict_list = "\n".join(text)


#OPENAI iniciation
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY") or "YOUR_API_KEY"

chat = ChatOpenAI(
    openai_api_key=os.environ["OPENAI_API_KEY"],
    model='gpt-3.5-turbo'
)

# create a new user prompt
augmented_prompt = f""" Usando el siguiente context necesito que agrupes en una cadena de texto la información que pertenecen a un mismo producto, y me regreses una lista de python con todos los productos con la informacion de un producto por posición

Contexts:
{prodict_list}

"""
prompt = HumanMessage(
    content=augmented_prompt

)

res = chat(prompt)

#save results
with open("productos.txt", "w") as archivo:
    # Escribir cada elemento de la lista en una línea separada
    for elemento in res:
        archivo.write(elemento + "\n")
