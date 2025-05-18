from fastapi import FastAPI
from app.api import upload

app = FastAPI(
    title="Riya's Wasserstoff AI Intern Task",
    description="Document Research & Theme Identification Chatbot",
    version="1.0.0"
)

# Register upload route
app.include_router(upload.router, prefix="/api", tags=["Upload"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Wasserstoff Internship Task API!"}
