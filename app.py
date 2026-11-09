from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
from rag_engine import DomainRAGEngine
import os

app = FastAPI(
    title="Enterprise Policy RAG Bot",
    description="Local-first RAG chatbot powered by FastAPI, Sentence-Transformers, and Google Gemini.",
    version="1.0.0",
)

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the RAGEngine and load documents on startup
rag_engine = DomainRAGEngine()
rag_engine.initialize_knowledge_base()


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: list[str]


@app.get("/")
def serve_ui():
    index_path = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(index_path):
        return FileResponse(index_path)
    return {
        "status": "online",
        "documents_loaded": len(rag_engine.documents),
        "message": "index.html not found. Please place index.html in the project folder."
    }


@app.post("/query", response_model=QueryResponse)
def query_knowledge_base(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    
    result = rag_engine.query(request.query)
    return QueryResponse(
        answer=result["answer"],
        sources=result["sources"]
    )