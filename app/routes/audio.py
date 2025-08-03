from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.audio_service import translate_audio, transcribe_audio

router = APIRouter()
    
@router.post("/transcribe-audio/")
async def transcribe_uploaded_audio_file(file: UploadFile = File(...)):
    """
    Transcribes an uploaded audio file using Azure OpenAI Whisper model.
    """
    try:
        transcript = await transcribe_audio(file)
        return {
            "file_name": file.filename,
            "transcription": transcript
        }
    except Exception as e:
        return {"error": str(e)}
    
@router.post("/translate-audio/")
async def translate_uploaded_audio_file(file: UploadFile = File(...)):
    """
    translate(language converion) an uploaded audio file using Azure OpenAI Whisper model.
    """
    try:
        result = await translate_audio(file)
        return {
            "file_name": file.filename,
            "translated_text": result
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
