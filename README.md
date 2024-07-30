Here is a README description for your GitHub repository:

---

# Bruno Child Offers Chatbot

This repository contains the code for the Bruno Child Offers Chatbot, an AI-powered assistant built using Streamlit and LangChain. The chatbot interacts with users, answering their questions by leveraging OpenAI's GPT-3.5-turbo model and Pinecone for vector storage and retrieval. Before running the local 

## Directory Structure

```
project/
├── utils/
│   ├── __init__.py
│   ├── helpers.py
├── streamlit/
│   ├── __init__.py
│   ├── main.py
└── src/
    ├── chatbots/
        ├── streamlit_chatbot.pyCertainly! Here’s the updated README with the image included:
```

---

# Bruno Child Offers Chatbot

This repository contains the code for the Bruno Child Offers Chatbot, an AI-powered assistant built using Streamlit and LangChain. The chatbot interacts with users, answering their questions by leveraging OpenAI's GPT-3.5-turbo model and Pinecone for vector storage and retrieval.

![Chatbot Screenshot](https://github.com/RaquelVaCorr/ProductChatBot/blob/main/src/images/screenshot_chatbot.png)

## Features

- **Streamlit Integration**: Provides a web interface for interacting with the chatbot.
- **LangChain**: Utilizes LangChain for chat models and embeddings.
- **OpenAI GPT-3.5-turbo**: Powers the chatbot's conversational abilities.
- **Pinecone**: Used for storing and retrieving embeddings.

## Setup

### Prerequisites

- Python 3.8+
- Streamlit
- OpenAI API Key
- Pinecone API Key

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/RaquelVaCorr/ProductChatBot.git
    cd your-repo
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your API keys:

    ```env
    PC_API_KEY=your_pinecone_api_key
    OPENAI_API_KEY=your_openai_api_key
    ```

5. Place your data files in the appropriate directories:
    - `datasources/json/keys.json`

6. Verify the next file exist. It is a digitalization of data of the catalog located in `datasources/pdf/Bruno_child_offers.pdf`. In case the nex file does not exist, then run first `src\preprocessing\main.py`:
    - `datasources/json/productos.json`

### Running the Chatbot

1. Navigate to the `streamlit` directory:

    ```bash
    cd streamlit
    ```

2. Run the Streamlit application:

    ```bash
    streamlit run main.py
    ```

3. Open your browser and go to `http://localhost:8501` to interact with the chatbot.

## Usage

1. Open the Streamlit application in your browser.
2. Enter your query in the input box and press Enter.
3. The chatbot will generate a response using the AI model and display it on the screen.

## File Overview

### `streamlit_chatbot.py`

This script sets up the Streamlit interface and integrates various components:

- **Imports and Environment Setup**: Loads environment variables and necessary libraries.
- **Data Loading**: Loads product data and API keys from JSON files.
- **Pinecone and OpenAI Initialization**: Initializes Pinecone for vector storage and sets up the OpenAI GPT-3.5-turbo model.
- **Embeddings and Vectorstore**: Creates embeddings from the product data and sets up the vector store.
- **Streamlit UI**: Defines the user interface for interacting with the chatbot, including message handling and displaying responses.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License.


