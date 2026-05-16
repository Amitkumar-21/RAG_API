import chromadb

client = chromadb.PersistentClient(path="data/chroma")

collection = client.get_or_create_collection(
    name="documents"
)

def store_chunks(chunks, filename, generate_embedding):
    for i, chunk in enumerate(chunks):
        embedding = generate_embedding(chunk)
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{filename}_{i}"],
            metadatas=[
                {
                    "source": filename,
                    "chunk_index": i
                }
            ]
        )