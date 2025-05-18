from fastapi import APIRouter, Query
from sentence_transformers import SentenceTransformer
import chromadb

router = APIRouter()

# Load the same model and ChromaDB client
model = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.Client()
collection = client.get_or_create_collection("documents")

@router.get("/search/")
async def search_documents(query: str = Query(..., description="Your natural language question")):
    # Step 1: Embed the query
    query_embedding = model.encode(query).tolist()

    # Step 2: Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )

    # Step 3: Format the output
    final_results = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        final_results.append({
            "chunk_text": doc,
            "doc_id": meta.get("doc_id"),
            "chunk_index": meta.get("chunk_index")
        })

    return {
        "query": query,
        "results": final_results
    }
