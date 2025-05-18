from fastapi import FastAPI
from app.api import upload, query  # <- ADD this

app = FastAPI(
    title="Wasserstoff AI Intern Task",
    description="Document Research & Theme Identification Chatbot",
    version="1.0.0"
)

app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(query.router, prefix="/api", tags=["Search"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Riya's Internship Task API!"}
