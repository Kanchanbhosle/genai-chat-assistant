GenAI Chat Assistant (RAG-Based)

A Retrieval-Augmented Generation (RAG) chatbot built using Python and Flask.
This system retrieves relevant documents from a knowledge base and uses a local language model to generate accurate answers.

The chatbot runs locally using Ollama and a lightweight LLM.

Architecture Diagram

Below is the architecture of the RAG system used in this project.

Flow:

User Question
     ↓
Flask Web Interface
     ↓
Embedding Model (SentenceTransformer)
     ↓
Cosine Similarity Search
     ↓
Top-K Document Retrieval
     ↓
Prompt Construction
     ↓
LLM via Ollama
     ↓
Generated Response

RAG Workflow Explanation

The system follows the Retrieval-Augmented Generation pipeline:

User asks a question in the web interface.

The question is converted into an embedding using SentenceTransformers.

The query embedding is compared with document embeddings stored in the knowledge base.

Cosine similarity is used to find the most relevant documents.

The Top-K most relevant documents are retrieved.

These documents are inserted into the prompt as context.

The prompt is sent to the language model running through Ollama.

The model generates an answer using the retrieved context.

The answer is displayed in the chatbot UI.

This approach improves answer quality because the model is guided by relevant external knowledge.

Embedding Strategy

The project uses the embedding model:

all-MiniLM-L6-v2

from SentenceTransformers.

Reasons for choosing this model:

Fast and lightweight

Good semantic similarity performance

Works well on CPU

Suitable for small RAG applications

Each document from docs.json is converted into a vector embedding which represents its semantic meaning.

Example document:

Retrieval Augmented Generation improves language models by retrieving relevant documents from a knowledge base.
Similarity Search Explanation

To find relevant documents, the system uses cosine similarity implemented with scikit-learn.

Concept:

Similarity(Query, Document) = cosine(query_vector, document_vector)

Steps:

Convert the user query into an embedding.

Compare it with stored document embeddings.

Rank documents by similarity score.

Retrieve the Top-3 documents.

Using multiple documents improves context quality and reduces hallucinations.

Prompt Design Reasoning

The system uses a structured prompt so the language model answers using the retrieved context.

Example prompt:

You are a helpful AI assistant.

Answer the question ONLY using the information provided in the context.

Context:
{retrieved_documents}

Question:
{user_question}

Answer:

Prompt design goals:

Reduce hallucinations

Force the model to use retrieved knowledge

Provide clear instructions to the LLM

Technologies Used

Python

Flask

SentenceTransformers

scikit-learn

NumPy

Ollama

Project Structure
genai-chat-assistant
│
├── app.py
├── docs.json
├── requirements.txt
│
├── templates
│   └── index.html
│
├── static
│   └── styles.css
│
├── architecture.png
│
└── README.md
Setup Instructions

Follow these steps to run the chatbot locally.

1 Install Dependencies
pip install -r requirements.txt
2 Install Ollama

Download Ollama from:

https://ollama.ai

Install it on your system.

3 Download the Language Model

Run:

ollama pull tinyllama

This downloads the software model used by the chatbot.

4 Run the Application

Start the Flask server:

python app.py
5 Open the Chatbot

Open your browser and go to:

http://127.0.0.1:5000
Example Questions

Try asking questions such as:

What is Retrieval Augmented Generation?
How can I reset my password?
How do I create an account?
How can I contact support?
Features

Retrieval-Augmented Generation chatbot

Local LLM execution

Semantic search using embeddings

Top-K document retrieval

Flask web interface

Knowledge-based responses

Future Improvements

Possible improvements:

Add a vector database like FAISS

Improve UI with a modern chat interface

Add conversation memory

Deploy the chatbot to cloud platform