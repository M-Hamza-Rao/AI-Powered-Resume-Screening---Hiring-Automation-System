import chromadb
from chromadb.config import Settings

client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="cv_data")


def store_embeddings(chunks, embeddings):
    # delete existing data safely
    existing = collection.get()
    if existing["ids"]:
        collection.delete(ids=existing["ids"])

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[str(i)]
        )


def retrieve(query_embedding, top_k=3):
    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )
    return results['documents']
