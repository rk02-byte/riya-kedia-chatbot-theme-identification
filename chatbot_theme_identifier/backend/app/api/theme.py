from fastapi import APIRouter, Body
from typing import List
import os
from dotenv import load_dotenv
from groq import Groq

router = APIRouter()

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=GROQ_API_KEY)

@router.post("/theme/")
async def identify_themes(chunks: List[str] = Body(..., description="List of text chunks from different documents")):
    prompt = f"""
You are an AI assistant. Analyze the following document excerpts and group them into common themes.
For each theme:
- Give it a title
- Write a short summary
- Mention the chunk index or a short excerpt as reference.

Document Chunks:
{chunks}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a theme analysis assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=800
    )

    return {
        "themes": response.choices[0].message.content
    }
