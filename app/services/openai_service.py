# Azure OpenAI integration
from openai import AzureOpenAI
from app.config import *

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version=API_VERSION
)

DEPLOYMENT_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL")

def ask_with_context(query, documents):
    context = "\n\n".join(documents)
    messages = [
        {"role": "system", "content": "Use the provided context to answer the question."},
        {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
    ]
    response = client.chat.completions.create(
        model=AZURE_OPENAI_MODEL,
        messages=messages
    )
    return response.choices[0].message.content

def query_openai(question: str, chunks: list) -> str:
    context = "\n".join(chunks)
    prompt = f"""Answer the question based on the context below.
    Context: {context}
    Question: {question}
    Answer:"""

    response = client.chat.completions.create(
        model=DEPLOYMENT_MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()
