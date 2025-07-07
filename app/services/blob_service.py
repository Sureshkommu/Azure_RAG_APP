# Azure Blob upload logic
from azure.storage.blob import BlobServiceClient
from fastapi import UploadFile
from app.config import AZURE_BLOB_CONN_STRING, BLOB_CONTAINER_NAME
from azure.storage.blob import BlobServiceClient
import textract  # or PyPDF2/docx2txt etc. based on file type
import os, tempfile

def upload_to_blob(file: UploadFile) -> str:
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN_STRING)
    container_client = blob_service_client.get_container_client(BLOB_CONTAINER_NAME)

    blob_client = container_client.get_blob_client(file.filename)
    blob_client.upload_blob(file.file, overwrite=True)

    return blob_client.url

def extract_text_from_blob(file_name: str) -> str:
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_BLOB_CONN_STRING)
    blob_client = blob_service_client.get_blob_client(container=BLOB_CONTAINER_NAME, blob=file_name)
    
    # Download file content to a temp file
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        tmp_file.write(blob_client.download_blob().readall())
        tmp_path = tmp_file.name

    # Extract text
    try:
        text = textract.process(tmp_path).decode("utf-8")
    except Exception:
        text = ""

    os.remove(tmp_path)
    return text


