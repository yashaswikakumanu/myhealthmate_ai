from .vectorstore import load_vector_store

def get_relevant_docs(query, k=4):
    db = load_vector_store()
    return db.similarity_search(query, k=k)