from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rag_engine import DomainRAGEngine

rag_engine = DomainRAGEngine()

@asynccontextmanager
async def lifespan(app: FastAPI):
    rag_engine.initialize_knowledge_base()
    yield

app = FastAPI(
    title="Domain-Specific RAG Chatbot Service",
    description="Enterprise-grade RAG pipeline running locally for free.",
    lifespan=lifespan
)

class QueryPayload(BaseModel):
    query: str

@app.post("/api/v1/chat")
async def chat_endpoint(payload: QueryPayload):
    try:
        response = rag_engine.query(payload.query)
        return {"status": "success", "data": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))