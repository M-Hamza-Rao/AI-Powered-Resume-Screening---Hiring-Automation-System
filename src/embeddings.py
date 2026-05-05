from sentence_transformers import SentenceTransformer
import streamlit as st

@st.cache_resource
def load_model():
    return SentenceTransformer('all-MiniLM-L6-v2')

def generate_embeddings(chunks):
    model = load_model()
    embeddings = model.encode(chunks)
    return embeddings
