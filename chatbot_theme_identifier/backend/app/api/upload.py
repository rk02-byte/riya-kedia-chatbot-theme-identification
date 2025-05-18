from fastapi import APIRouter, UploadFile, File
import fitz  # PyMuPDF
from PIL import Image
import pytesseract
import os
import uuid

from app.services.embedding import embed_and_store

router = APIRouter()

# Get the current directory of this file (i.e., backend/app/)
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up one level to reach backend/, then define the data folder
UPLOAD_DIR = os.path.abspath(os.path.join(CURRENT_DIR, "..", "data"))
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Always resolve the path relative to the current file's location
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#UPLOAD_DIR = os.path.join(BASE_DIR, "data")
#os.makedirs(UPLOAD_DIR, exist_ok=True)

#UPLOAD_DIR = "backend/data/"
#os.makedirs(UPLOAD_DIR, exist_ok=True)

# Optional fallback for pytesseract if needed:
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@router.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Save the uploaded file
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract text from the file
    text = ""

    if file.filename.lower().endswith(".pdf"):
        doc = fitz.open(file_location)
        for page in doc:
            text += page.get_text()
    elif file.filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image = Image.open(file_location)
        text = pytesseract.image_to_string(image)
    else:
        return {"error": "Unsupported file type"}

    # Save text file (optional step for debugging)
    text_file = os.path.join(UPLOAD_DIR, file.filename + ".txt")
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(text)

    # Generate a document ID and store in vector DB
    doc_id = str(uuid.uuid4())
    num_chunks = embed_and_store(text, doc_id)

    return {
        "filename": file.filename,
        "text_preview": text[:500],
        "chunks_stored": num_chunks,
        "doc_id": doc_id
    }
