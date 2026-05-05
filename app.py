import streamlit as st
import json

from src.extraction import extract_text, clean_text
from src.chunking import chunk_text
from src.embeddings import generate_embeddings
from src.retrieval import store_embeddings, retrieve
from src.llm import evaluate_cv

st.title("AI Resume Screening System")

# Upload CV
cv_file = st.file_uploader("Upload CV (PDF)", type=["pdf"])

# Job Description
job_description = st.text_area("Paste Job Description")

# Model selection
mode = st.selectbox("Select Model", ["groq", "openai"])

if st.button("Analyze"):
    if cv_file and job_description:

        # Save uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(cv_file.read())

        # Pipeline
        text = extract_text("temp.pdf")
        cleaned = clean_text(text)
        chunks = chunk_text(cleaned)
        embeddings = generate_embeddings(chunks)

        store_embeddings(chunks, embeddings)

        query_embedding = generate_embeddings([job_description])[0]
        results = retrieve(query_embedding)

        evaluation = evaluate_cv(job_description, results, mode=mode)

        # Convert JSON string → dict
        if evaluation.startswith("Error"):
            st.error(evaluation)
        else:
            try:
                structured = json.loads(evaluation)
        
                st.subheader("Match Score")
                st.write(structured["score"])
        
                st.subheader("Strengths")
                for s in structured["strengths"]:
                    st.write("- " + s)
        
                st.subheader("Missing Skills")
                for m in structured["missing_skills"]:
                    st.write("- " + m)
        
                st.subheader("Suggestions")
                for s in structured["suggestions"]:
                    st.write("- " + s)
        
            except:
                st.error("Invalid response from model")

        # Display
        st.subheader("Match Score")
        st.write(structured["score"])

        st.subheader("Strengths")
        for s in structured["strengths"]:
            st.write("- " + s)

        st.subheader("Missing Skills")
        for m in structured["missing_skills"]:
            st.write("- " + m)

        st.subheader("Suggestions")
        for s in structured["suggestions"]:
            st.write("- " + s)

    else:
        st.warning("Please upload CV and enter job description")
