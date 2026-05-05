import chromadb
from chromadb.config import Settings

# initialize database
client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="cv_data")


def store_embeddings(chunks, embeddings):
    # clear previous data (important for Streamlit reruns)
    collection.delete(where={})

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
