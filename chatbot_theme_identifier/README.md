# Document Research & Theme Identification Chatbot

This is the internship assessment project for the AI Intern role at **Wasserstoff**.  
The project allows users to upload multiple documents (PDFs or images), ask natural language questions across them, and receive theme-based insights with cited document excerpts.

---
## 🔗 Live Demo

- **Frontend (Streamlit App)**: [Open App](https://riya-kedia-document-research-theme-identification-chatbot.streamlit.app/)

---

## Features

-  Upload multiple PDF or image documents
-  Extracts text using **OCR (Tesseract)** or PDF parsing
-  Stores chunked document embeddings using **ChromaDB**
-  Query documents semantically using **Sentence Transformers**
-  Synthesizes themes from top chunks using **LLAMA3 (via Groq)**
-  Citations provided using document IDs and excerpts

---

##  Tech Stack

- **Backend**: FastAPI, Uvicorn
- **OCR**: Tesseract, PyMuPDF
- **LLM**: Groq (LLAMA3)
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2)
- **Vector DB**: ChromaDB 
- **Frontend**: Streamlit 
- **Deployment**:  Backend: Render · Frontend: Streamlit Cloud

---
##  How It Works

1. **Upload Documents**  
   - PDFs parsed with PyMuPDF  
   - Images passed through Tesseract OCR  
   - Text is chunked and stored with embeddings in ChromaDB

2. **Ask a Question**  
   - User submits a natural language query  
   - Query embedding is compared to stored document chunks  
   - Top `k` results are returned with `doc_id` and preview

3. **Generate Themes**  
   - Top chunks are passed to Groq’s LLAMA3 model  
   - Model groups results into themes  
   - Each theme includes a summary and excerpts for citation

---

##  Project Structure
chatbot_theme_identifier/
│
├── backend/ ← FastAPI backend (API, OCR, embeddings)
│ ├── app/
│ │ ├── api/ ← Upload, search, theme routes
│ │ ├── services/ ← Embedding and storage logic
│ │ └── main.py ← FastAPI entry point
│ ├── data/ ← Uploaded docs and chunk storage
│ ├── requirements.txt
│ └── start.sh
│
├── frontend/ ← Streamlit app
│ └── app.py
---

##   Local Setup Instructions

```bash
# Clone the repo
cd chatbot_theme_identifier

# Backend setup
cd backend
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend setup
cd ../frontend
streamlit run app.py



