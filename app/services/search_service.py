# Azure Cognitive Search integration
import requests
from app.config import AZURE_SEARCH_ENDPOINT, AZURE_SEARCH_KEY, AZURE_SEARCH_INDEX

def search_documents(query: str):
    url = f"{AZURE_SEARCH_ENDPOINT}/indexes/{AZURE_SEARCH_INDEX}/docs/search?api-version=2024-12-01-preview"
    headers = {
        "Content-Type": "application/json",
        "api-key": AZURE_SEARCH_KEY
    }
    payload = {
        "search": query,
        "top": 5
    }
    res = requests.post(url, headers=headers, json=payload)
    docs = res.json().get("value", [])
    return [doc.get("content", "") for doc in docs]
