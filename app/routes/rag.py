 # Upload, search, and ask endpoints
from fastapi import APIRouter, File, UploadFile, Query
from app.services import search_service, openai_service
from app.services.blob_service import upload_to_blob
import uuid
from pydantic import BaseModel
from app.services.blob_service import extract_text_from_blob
from app.utils.file_utils import chunk_text
from app.services.openai_service import query_openai


router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    # Save to Azure Blob
    file_url = upload_to_blob(file)
    return {
        "message": "File uploaded successfully",
        "file_name": file.filename,
        "url": file_url
    }

class AskResponse(BaseModel):
    id: str
    question: str
    answer: str
    file_name: str

@router.get("/ask/", response_model=AskResponse)
async def ask(question: str = Query(...), file_name: str = Query(...)):
    # Load document from blob or cache
    content = extract_text_from_blob(file_name)
    chunks = chunk_text(content)
    answer = query_openai(question, chunks)

    # Generate unique ID
    response_id = str(uuid.uuid4())

    return {
        "id": response_id,
        "question": question,
        "answer": answer,
        "file_name": file_name
    }
