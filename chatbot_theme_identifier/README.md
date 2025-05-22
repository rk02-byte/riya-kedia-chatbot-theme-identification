# Document Research and Theme Identification Chatbot

This repository contains my submission for the AI Internship Task at Wasserstoff Innovation and Learning Labs. The project implements a system that allows users to upload multiple documents, ask semantic questions across them, and receive summarized themes with citations. The full-stack application is deployed and publicly accessible.

---

## Live Deployment

- **Frontend (Streamlit Application)**: [View Live App](https://riya-kedia-document-research-theme-identification-chatbot.streamlit.app/)
---

## Features

- Upload multiple PDF or image documents
- Extract text using OCR (Tesseract) or PDF parsing
- Chunk and embed documents using sentence-transformers
- Store and query embeddings using ChromaDB
- Ask natural language questions to retrieve relevant document chunks
- Generate theme-based summaries from retrieved chunks using the LLAMA3 model (via Groq API)
- Include document-level citation mapping for transparency

---

## Technology Stack

**Backend:**
- Python 3.10
- FastAPI
- Tesseract OCR (via pytesseract)
- PyMuPDF (for PDF parsing)
- SentenceTransformers (MiniLM model)
- ChromaDB (for vector storage)
- Groq API (LLAMA3 for theme generation)
- Uvicorn (server)

**Frontend:**
- Streamlit

**Hosting:**
- Render (Backend)
- Streamlit Cloud (Frontend)

---

## System Workflow

1. **Document Upload**  
   Users can upload one or more PDF/image files. Text is extracted using either OCR or direct PDF parsing, then chunked and embedded.

2. **Semantic Search**  
   Users submit a query. The system compares the query's embedding with stored chunks to retrieve the most relevant sections.

3. **Theme Synthesis**  
   Retrieved chunks are passed to a language model (LLAMA3 via Groq) to produce theme-based summaries with cited excerpts.
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
   - 
##  Project Structure

```
chatbot_theme_identifier/
│
├── backend/ # Backend (FastAPI)
│ ├── app/
│ │ ├── api/ # API routes: upload, search, theme
│ │ ├── services/ # Embedding and storage logic
│ │ └── main.py # FastAPI app entry point
│ ├── data/ # Uploaded documents and chunked text
│ ├── requirements.txt
│ └── start.sh # Startup script for Render
│
├── frontend/ # Frontend (Streamlit)
│ └── app.py # Streamlit interface
```
## Setup Instructions (Local Development)

### Backend (FastAPI)

```bash
cd chatbot_theme_identifier/backend
python -m venv venv
venv\Scripts\activate            # On Windows
pip install -r requirements.txt
uvicorn app.main:app --reload

```
### Frontend setup
```bash
cd chatbot_theme_identifier/frontend
streamlit run app.py

```

## API Endpoints
```bash
POST	/api/upload/	
GET	/api/search/	
POST	/api/theme/

```

