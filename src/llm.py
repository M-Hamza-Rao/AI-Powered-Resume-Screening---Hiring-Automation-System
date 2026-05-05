from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

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
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    elif mode == "groq":
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    else:
        raise ValueError("Invalid mode")