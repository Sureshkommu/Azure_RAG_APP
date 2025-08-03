from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.mix_models import transcribe_and_summarize

router = APIRouter()

@router.post("/summarize-audio/")
async def summarize_audio(file: UploadFile = File(...)):
    try:
        result = await transcribe_and_summarize(file)
        return {
            "file_name": file.filename,
            "summary": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {e}")
