from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import os

DATA_PATH = "data"
DB_PATH = "vector_db"

def ingest_documents():
    docs = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(DATA_PATH, file))
            docs.extend(loader.load())

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()

    db = FAISS.from_documents(chunks, embeddings)

    db.save_local(DB_PATH)

    print("Vector DB created!")

if __name__ == "__main__":
    ingest_documents()