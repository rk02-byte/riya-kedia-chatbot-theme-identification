# Document Research & Theme Identification Chatbot

This is the internship assessment project for the AI Intern role at **Wasserstoff**.  
It involves building a web-based chatbot that performs research over a large set of documents, extracts cited responses, and identifies common themes.

---

##  Features

-  Upload 75+ documents (PDFs, scanned images)
-  OCR support for scanned documents
-  Document storage and processing into a semantic knowledge base
-  Natural language query interface
-  Extracts responses with **document-level citations**
-  Theme identification across multiple documents
-  Synthesized responses showing coherent themes
-  Public deployment with a clean UI

---

##  Tech Stack

- **Backend**: Python, FastAPI
- **OCR**: Tesseract
- **LLMs**: Groq (LLAMA3)
- **Vector DB**: ChromaDB 
- **Frontend**: Streamlit 
- **Deployment**: Render / Hugging Face Spaces

---

##  Folder Structure
chatbot_theme_identifier/
├── backend/
│ ├── app/
│ │ ├── api/
│ │ ├── core/
│ │ ├── models/
│ │ ├── services/
│ │ ├── main.py
│ │ └── config.py
│ ├── data/
│ ├── Dockerfile
│ └── requirements.txt
├── docs/
├── tests/
├── demo/
└── README.md


---

##  Setup Instructions

1. Create a virtual environment:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    ```

2. Install dependencies:
    ```bash
    pip install -r backend/requirements.txt
    ```

3. Run the server:
    ```bash
    uvicorn app.main:app --reload --app-dir backend/app
    ```

4. Open in browser: [http://127.0.0.1:8000](http://127.0.0.1:8000)



