from langchain.document_loaders import PyPDFLoader
import os

def load_medical_docs(folder_path):
    docs = []
    for file in os.listdir(folder_path):
        if file.endswith(".pdf"):
            path = os.path.join(folder_path, file)
            loader = PyPDFLoader(path)
            docs.extend(loader.load())
    return docs