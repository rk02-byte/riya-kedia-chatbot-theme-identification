from fastapi import APIRouter, Body
from typing import List
import os
from dotenv import load_dotenv
from groq import Groq
import json
import re

router = APIRouter()

# Load environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#Groq API key
client = Groq(api_key=GROQ_API_KEY)

@router.post("/theme/")
async def identify_themes(chunks: List[str] = Body(..., description="List of text chunks from documents")):
    prompt = f"""
You are an AI assistant.

Given a list of document excerpts, your task is to group them into coherent themes.

For each theme:
- Give a concise title (3–5 words)
- Write a short summary
- Include the most relevant excerpts that support the theme

IMPORTANT:
Format your answer as **JSON only**, with no extra explanation or headers.
Use the structure below exactly:

{{
  "Theme 1": {{
    "title": "Short Title",
    "summary": "Brief explanation of the theme...",
    "chunks": ["excerpt 1", "excerpt 2", ...]
  }},
  ...
}}

Document Chunks:
{chunks}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a theme analysis assistant. Output ONLY JSON."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=1000
    )

    raw_response = response.choices[0].message.content.strip()

    # extracting JSON block from the response using regex
    try:
        json_string = re.search(r"\{[\s\S]*\}", raw_response).group()
        parsed = json.loads(json_string)
        return {"themes": parsed}
    except Exception as e:
        return {
            "themes": {
                "raw": raw_response,
                "error": f"Response could not be parsed as JSON. Error: {str(e)}"
            }
        }
