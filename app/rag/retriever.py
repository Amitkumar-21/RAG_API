from app.db.vector_store import collection
from app.rag.embedder import generate_embedding

def retrieve_chunks(query, top_k=3):
    query_embedding = generate_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results["documents"][0]