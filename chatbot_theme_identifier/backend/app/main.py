from fastapi import FastAPI
from app.api import upload, query, theme
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Wasserstoff AI Intern Task",
    description="Document Research & Theme Identification Chatbot",
    version="1.0.0"
)
#CORS error
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://riya-document-research-theme-7iie.onrender.com"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api", tags=["Upload"])
app.include_router(query.router, prefix="/api", tags=["Search"])
app.include_router(theme.router, prefix="/api", tags=["Theme"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Riya's Internship Task API!"}
