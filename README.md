# AI Lawyer Chatbot

## Project Overview

This project implements an AI-powered chatbot designed to assist with legal queries, specifically focusing on human rights. It leverages Retrieval-Augmented Generation (RAG) to provide accurate and contextually relevant information by combining the power of large language models with a robust vector database built from legal documents.

## How It Works

The chatbot operates through the following key components:

1.  **PDF Ingestion and Processing**: The system can ingest PDF documents, such as the "Universal Human Rights" document, and process them into manageable chunks.
2.  **Vector Database Creation**: These processed text chunks are then converted into numerical vector embeddings using a pre-trained model. These embeddings are stored in a vector database (e.g., ChromaDB) for efficient similarity searches.
3.  **RAG Pipeline**: When a user asks a question, the RAG pipeline performs the following steps:
    *   **Retrieval**: The user's query is also converted into an embedding, which is then used to search the vector database for the most relevant document chunks.
    *   **Augmentation**: The retrieved relevant chunks are then provided as context to a large language model (LLM).
    *   **Generation**: The LLM uses this context, along with its general knowledge, to generate a comprehensive and accurate answer to the user's query.
4.  **Frontend Interface**: A simple web-based frontend allows users to interact with the chatbot, type their queries, and receive responses.

## Technologies Used

*   **Python**: The core programming language for the backend logic.
*   **LangChain**: A framework for developing applications powered by language models. It's used for chaining together various components of the RAG pipeline.
*   **ChromaDB**: A vector database used to store and retrieve document embeddings efficiently.
*   **Streamlit**: For creating the interactive web-based frontend (based on `frontend.py`).
*   **Hugging Face Embeddings**: For generating vector embeddings from text.
*   **Large Language Models (LLMs)**: Utilized for generating responses, potentially integrated via APIs (e.g., OpenAI, Google Gemini, or a local open-source LLM).
*   **As of now I'm not connecting any direct DB to the project it the vector stores are stored in the directory.

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository**:
    ```bash
    git clone <your-repository-url>
    cd <your-project-directory>
    ```
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    ```
3.  **Activate the virtual environment**:
    *   On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
4.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
5.  **Environment Variables**: Create a `.env` file in the root directory of the project and add your API keys (e.g., for OpenAI, Google Gemini) if required by the LLM you choose to use.
    ```
    # Example for OpenAI API Key
    GROQ_API_KEY="your_groq_api_key_here"
    ```
6.  **Prepare PDF Documents**: Place your PDF documents (e.g., `universal_human_rights.pdf`) in the `pdfs/` directory. The system is designed to read from this directory.
7.  **Run the Vector Database Ingestion**: This step will process your PDFs and populate the vector database.
    ```bash
    python vector_database.py
    ```
8.  **Start the Frontend Application**:
    ```bash
    python frontend.py
    ```
    (Note: If `frontend.py` uses Streamlit, you might need to run `streamlit run frontend.py` instead.)

## Project Structure

*   `requirements.txt`: Lists all the Python dependencies.
*   `frontend.py`: Contains the code for the web-based user interface.
*   `rag_pipeline.py`: Implements the Retrieval-Augmented Generation logic.
*   `vector_database.py`: Handles PDF ingestion, text chunking, embedding generation, and vector database operations.
*   `univeral_human_rights.pdf`: Example PDF document used for populating the knowledge base.
*   `pdfs/`: Directory to store additional PDF documents.
*   `vectorstore/`: Directory where the vector database will be stored (ignored by Git).
*   `.env`: Environment variables for API keys (ignored by Git).
*   `.gitignore`: Specifies files and directories to be ignored by Git.

## Screenshots / Images

In the images folder of my project, I will add a screenshots when I'm running this project. I have not deployed ecause of OLLAMA, so that's why I run the project on local host, take screenshots and added that screenshots in my images folder. So you can also use this project just replace the actual api-key of yours using GroqClloud.

## Future Enhancements

*   Add support for more document types (e.g., DOCX, TXT).
*   I also want to add multimodels in this project.
*   Implement user authentication and multi-user support.
