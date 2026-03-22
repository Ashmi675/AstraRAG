# AstraRAG

AstraRAG is an Agentic Retrieval-Augmented Generation (RAG) chatbot that allows users to query documents and receive context-aware answers using Large Language Models.

The system retrieves relevant information from uploaded documents and generates intelligent responses using an AI pipeline.

---

## Features

- Document ingestion from PDFs
- Semantic search using vector embeddings
- Retrieval-Augmented Generation (RAG)
- Interactive chatbot interface
- Fast vector search using FAISS
- Streamlit-based UI

---

## Architecture

User Query  
↓  
Retriever (Vector Database - FAISS)  
↓  
Relevant Document Chunks  
↓  
LLM generates response  

---

## Project Structure

AstraRAG  
│  
├── app.py  
├── requirements.txt  
├── Dockerfile  
├── README.md  
│  
├── agents  
│   ├── researcher.py  
│   ├── analyst.py  
│   └── writer.py  
│  
├── rag  
│   ├── ingest.py  
│   └── retriever.py  
│  
├── data  
│   └── documents  
│  
└── vector_db  

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/AstraRAG.git
cd AstraRAG
