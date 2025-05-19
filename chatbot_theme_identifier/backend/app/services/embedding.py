from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions
import uuid

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Setup ChromaDB in-memory 
client = chromadb.Client()
collection = client.get_or_create_collection("documents")

#chunk_index
def chunk_text(text: str, chunk_size: int = 500) -> list:
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def embed_and_store(text: str, doc_id: str):
    chunks = chunk_text(text)
    embeddings = model.encode(chunks).tolist()
    
    for idx, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
        collection.add(
            documents=[chunk],
            embeddings=[embedding],
            ids=[f"{doc_id}_{idx}"],
            metadatas=[{"doc_id": doc_id, "chunk_index": idx}]
        )
    
    return len(chunks)
