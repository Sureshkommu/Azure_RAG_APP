# FastAPI app entry point

from fastapi import FastAPI
from app.routes import rag

app = FastAPI(
    title="Azure Rag App",  # 👈 This sets the Swagger UI title
    description="Upload a file and ask questions using Azure RAG",
    version="1.0.0"
)

app.include_router(rag.router)

