from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Wasserstoff Internship Task API is running"}
