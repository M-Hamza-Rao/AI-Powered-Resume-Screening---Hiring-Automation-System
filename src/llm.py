from groq import Groq
import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

def get_key(name):
    return os.getenv(name) or st.secrets.get(name)


def evaluate_cv(job_description, retrieved_chunks, mode="groq"):
    context = "\n\n".join(retrieved_chunks[0])

    prompt = f"""
You are an AI hiring assistant.

Evaluate the candidate CV based on the job description.

Job Description:
{job_description}

Candidate CV:
{context}

Return ONLY valid JSON in this exact format (no extra text):

{{
  "score": number between 0 and 100,
  "strengths": ["point1", "point2"],
  "missing_skills": ["point1", "point2"],
  "suggestions": ["point1", "point2"]
}}
"""

    if mode == "openai":
        from openai import OpenAI, AuthenticationError

        api_key = get_key("OPENAI_API_KEY")
        if not api_key:
            return "Error: OPENAI_API_KEY not found."

        client = OpenAI(api_key=api_key)

        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content

        except AuthenticationError:
            return "Error: Invalid or expired OpenAI API key."

        except Exception as e:
            return f"Error: OpenAI request failed - {str(e)}"

    elif mode == "groq":
        api_key = get_key("GROQ_API_KEY")
        if not api_key:
            return "Error: GROQ_API_KEY not found."

        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    else:
        return "Error: Invalid mode"
