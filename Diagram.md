+--------------------+
| Load Environment   |
| Variables (dotenv) |
+--------------------+
          |
          v
+---------------------+
| Load Data from JSON |
| (productos.json &   |
|  keys.json)         |
+---------------------+
          |
          v
+-----------------------------+
| Initialize Pinecone &       |
| OpenAI Instances            |
+-----------------------------+
          |
          v
+-----------------------------+
| Setup Chat Model (OpenAI)   |
+-----------------------------+
          |
          v
+-----------------------------+
| Setup Embedding Model       |
+-----------------------------+
          |
          v
+-----------------------------+
| Create Embeddings           |
| (using OpenAIEmbeddings)    |
+-----------------------------+
          |
          v
+-----------------------------+
| Create Vectorstore          |
+-----------------------------+
          |
          v
+-----------------------------+
| Streamlit UI                |
| +-------------------------+ |
| | Title and Subheader     | |
| | Text Input for Queries  | |
| | Display Chat Messages   | |
| +-------------------------+ |
+-----------------------------+
          |
          v
+-----------------------------+
| User Query Handling         |
| +-------------------------+ |
| | Augment Prompt          | |
| | Generate Response       | |
| | Update Session State    | |
| +-------------------------+ |
+-----------------------------+
          |
          v
+-----------------------------+
| Display Chat Messages       |
+-----------------------------+
