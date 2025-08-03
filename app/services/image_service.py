from openai import AzureOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),  # Your Azure OpenAI API key  
    api_version="2024-04-01-preview",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT") # Your Azure OpenAI endpoint
)

def generate_image(prompt: str) -> str:
    response = client.images.generate(
        model = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"), # or "dall-e-2" depending on your deployment
        prompt = prompt,
        n = 1,
        size ="1024x1024"
    )
    return response.data[0].url
