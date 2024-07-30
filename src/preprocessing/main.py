import os
from pdfquery import PDFQuery
from openai import OpenAI
import re
import json


#preprocesing pdf
pdf = PDFQuery('Bruno_child_offers.pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]
prodict_list = "\n".join(text)
print(text)



#OpenAI initiation

client = OpenAI()

# Create user prompt
augmented_prompt = f"""Usando el siguiente contexto necesito que agrupes en una cadena de texto la información que pertenece a un mismo producto, y me regreses solamente una lista de python con todos los productos con la información de un producto por posición.

Contexto:
{prodict_list}

"""
response = client.chat.completions.create(
    model='gpt-4o',
    messages=[{"role": "user", "content": augmented_prompt}]
)

productos_string = response.choices[0].message.content

# Extracting the list of products from the string
pattern = re.compile(r'\[(.*)\]', re.DOTALL)
matches = pattern.search(productos_string)
products_str = matches.group(1).strip()
products_str = products_str.strip().split(',\n    ')

# Save to a JSON file
with open('.\datasources\json\productos.json', 'w') as file:
    json.dump(products_str, file)