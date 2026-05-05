# AI-Powered Resume Screening & Hiring Automation System

## Overview

This project is an end-to-end AI-powered resume screening system that evaluates candidate resumes against job descriptions using Retrieval-Augmented Generation (RAG) and Large Language Models (LLMs). The system automates candidate evaluation by generating a match score, identifying strengths and missing skills, and providing actionable recommendations.

The application processes unstructured PDF resumes, performs semantic retrieval, and uses LLMs to produce structured hiring insights through an interactive web interface.

---

## Key Features

- PDF resume parsing and text extraction
- Text preprocessing and normalization
- Semantic chunking using LangChain
- Embedding generation using sentence-transformers
- Vector similarity search using ChromaDB
- Retrieval-Augmented Generation (RAG) pipeline
- LLM-based evaluation using OpenAI or Groq
- Structured JSON output (score, strengths, gaps, suggestions)
- Interactive UI built with Streamlit
- Multi-model support (OpenAI and Groq)

---

## System Architecture


CV (PDF)
↓
Text Extraction (pdfplumber)
↓
Text Cleaning (regex)
↓
Chunking (LangChain)
↓
Embeddings (sentence-transformers)
↓
Vector Database (ChromaDB)
↓
Retrieval (Top-K relevant chunks)
↓
LLM Evaluation (OpenAI / Groq)
↓
Structured Output (JSON)
↓
Streamlit UI


---

## Technologies Used

- Python
- Streamlit
- pdfplumber
- LangChain
- sentence-transformers
- ChromaDB
- OpenAI API
- Groq API
- python-dotenv

---

## Installation

### 1. Clone the repository


git clone https://github.com/M-Hamza-Rao/AI-Powered-Resume-Screening---Hiring-Automation-System

cd AI-Powered-Resume-Screening---Hiring-Automation-System


---

### 2. Install dependencies


pip install -r requirements.txt


---

### 3. Set environment variables

Create a `.env` file in the root directory:


OPENAI_API_KEY=your_openai_key
GROQ_API_KEY=your_groq_key


Alternatively, for Streamlit Cloud, use `st.secrets`.

---

## Running the Application


streamlit run app.py


The application will be available at:


http://localhost:8501


---

## Usage

1. Upload a resume (PDF format)
2. Paste the job description
3. Select the LLM (OpenAI or Groq)
4. Click "Analyze"
5. View:
   - Match score
   - Strengths
   - Missing skills
   - Suggestions

---

## Output Format

The system produces structured output in JSON format:

```json
{
  "score": 85,
  "strengths": ["..."],
  "missing_skills": ["..."],
  "suggestions": ["..."]
}
Project Structure
resume-ai/
│
├── data/
├── src/
│   ├── extraction.py
│   ├── chunking.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── llm.py
│   ├── scoring.py
│
├── app.py
├── requirements.txt
├── README.md
Design Decisions
RAG architecture used to improve evaluation accuracy by focusing on relevant resume sections
LangChain used specifically for robust text chunking
ChromaDB used for lightweight and efficient vector storage
sentence-transformers chosen for fast and effective embedding generation
JSON output enforced to ensure reliable parsing and downstream usage
Multi-LLM support implemented to balance cost, performance, and accessibility
Limitations
LLM responses may vary depending on prompt quality
Free-tier API usage may be rate-limited
Resume formatting inconsistencies can affect extraction quality
Future Improvements
Resume keyword highlighting
ATS-style scoring system
Downloadable PDF report
Multi-candidate comparison dashboard
Improved section-based parsing
Fine-tuned domain-specific models
License

This project is for educational and demonstration purposes.