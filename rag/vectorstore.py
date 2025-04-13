from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
import os

EMBEDDING_MODEL = OpenAIEmbeddings()

def create_vector_store(docs, persist_dir="rag/faiss_index"):
    db = FAISS.from_documents(docs, EMBEDDING_MODEL)
    db.save_local(persist_dir)
    return db

def load_vector_store(persist_dir="rag/faiss_index"):
    return FAISS.load_local(persist_dir, EMBEDDING_MODEL)