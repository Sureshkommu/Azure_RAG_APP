# app/services/audio_service.py
from openai import AzureOpenAI
from fastapi import UploadFile
import os
import io
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_AUDIO"),
    api_version="2023-09-01-preview",
    api_key=os.getenv("AZURE_OPENAI_API_KEY_AUDIO")
)

async def transcribe_audio(file: UploadFile) -> str:
    contents = await file.read()
    file_io = io.BytesIO(contents)
    file_io.name = file.filename  # trick to help OpenAI determine format
    response = client.audio.transcriptions.create(
        model="audio-demo-whisper",
        file=file_io,
        response_format="text",
        language="en"
    )
    return response

async def translate_audio(file: UploadFile) -> str:
    contents = await file.read()
    file_io = io.BytesIO(contents)
    file_io.name = file.filename  # Helps OpenAI determine format

    response = client.audio.translations.create(
        model="audio-demo-whisper",
        file=file_io,
        response_format="text",
        #language="fr" # specify the language if known, e.g., "en" for sample_french.mp3(French)
    )
    return response
