import io
import os
from dotenv import load_dotenv
from fastapi import UploadFile
from openai import AzureOpenAI

load_dotenv()

# Azure OpenAI clients for Whisper (transcription) and GPT-4 (summarization)
client_transcribe = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_AUDIO"),
    api_version="2023-09-01-preview",
    api_key=os.getenv("AZURE_OPENAI_API_KEY_AUDIO")
)

client_summarize = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT_GPT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION_GPT", "2025-01-01-preview"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY_GPT")
)

async def transcribe_and_summarize(file: UploadFile) -> str:
    contents = await file.read()
    file_io = io.BytesIO(contents)
    file_io.name = file.filename

    # Step 1: Transcription via Whisper
    transcription = client_transcribe.audio.transcriptions.create(
        model="audio-demo-whisper",  # Must match your actual deployment name
        file=file_io,
        response_format="text"
    )

    # Step 2: Summarization via GPT-4
    response = client_summarize.chat.completions.create(
        model="text-demo-gpt-4.1",  # Must match your actual deployment name
        messages=[
            {
                "role": "user",
                "content": f"Summarize the following text to two bullet points:\n{transcription}"
            }
        ]
    )

    summary_text = response.choices[0].message.content

    # Optionally write to file
    with open("transcript_summarization.txt", "w", encoding="utf-8") as f:
        f.write(summary_text)

    return summary_text
