# Instructions

# 🚀 Azure RAG FastAPI App (No LangChain)

A lightweight Retrieval-Augmented Generation (RAG) backend using **FastAPI**, **Azure Blob Storage**, and **Cognitive Search**, **Azure OpenAI**. Upload Documents(PDF,DOCX,XLSX,CSV,etc.) This version does **not** use LangChain. Extract and search thier content. Generate answers using GPT based on file content.

1. Setup Virtual Environment
open your project folder path ex: cd D:\azure_rag_app
python -m venv ragvenv
ragvenv\Scripts\activate

2. Install Dependencies
pip install -r requirements.txt

4. Run the FastAPI App
uvicorn app.main:app --reload

✅ STEP-BY-STEP AZURE PORTAL UI GUIDE
🔹 1. Create a Resource Group
Go to https://portal.azure.com

In the search bar, type "Resource groups" → Click Create

Fill in:

Subscription: your active subscription

Resource group name: rag-demo-rg-cgs

Region: East US (or your preferred region)

Click Review + Create → Create

🔹 2. Set Up Azure Blob Storage
2.1 Create a Storage Account
Search for "Storage accounts" → Click Create

Fill in:

Resource group: rag-demo-rg-cgs

Storage account name: must be globally unique (e.g., ragstoragecgs)

Region: East US

Performance: Standard

Redundancy: Locally-redundant storage (LRS)

Click Review + Create → Create

2.2 Create a Blob Container
After deployment, go to your storage account(options is like 'data storage')

In the left menu, click Containers

Click + Container

click + add container

Name: cgs-files-documents

Public access level: Private (no anonymous access)

Click Create

2.3 Get the Connection String
In the data storage account or scurity + networking → Access keys

Click Show Keys

Copy the Connection String

✅ Save it as AZURE_BLOB_CONN_STRING

🔹 3. Set Up Azure Cognitive Search
3.1 Create the Search Service
Search for "Azure Cognitive Search or AI Search" → Click Create

Fill in:

Resource group: rag-demo-rg-cgs

Service name: e.g., ragsearchsvc (must be unique)

Region: East US

Pricing tier: Basic

Click Review + Create → Create

3.2 Get the Admin Key & Endpoint
Go to the created Search Service(e.g., ragsearchsvc)

Left menu click settings → Keys

Copy Admin key and Endpoint(click + overview copy url)

✅ Save:

AZURE_SEARCH_KEY

AZURE_SEARCH_ENDPOINT

3.3 Import Data to Create Index
In the search service overview → Click Import data

Choose:

Data Source: Azure Blob Storage

Authenticate using connection string

Choose your container: cgs-files-documents

Cognitive Skills:

Choose "Extract text and metadata"

Select built-in AI enrichment options (OCR, key phrases, etc.)

Create:

Skillset: leave default or name azureblob-skillset

Index: e.g., azureblob-skillset

Indexer: e.g., rag-indexer

Click Submit

✅ Save:

AZURE_SEARCH_INDEX = azureblob-skillset

🔹 4. Set Up Azure OpenAI (GPT)
4.1 Apply for Access (if not yet)
Go to: https://aka.ms/oai/access

Apply with your use case and wait for approval

4.2 Create Azure OpenAI Resource
In Azure Portal → Click Create a resource

Search for Azure OpenAI or Azure AI

Click Create

Fill:

Resource group: rag-demo-rg-cgs

Name: rag-openai

Region: East US (must support OpenAI)

Pricing tier: Standard S0

Click Review + Create → Create

4.3 Deploy a Model (GPT)
Go to the Azure OpenAI resource

Click Azure OpenAI studio or Azure AI Foundry portal 
Click + create new Deployments
or 
Click + Create

Choose:

Model: gpt-35-turbo (or gpt-4o)

Deployment name: gpt35 or gpt4(gpt-4o)

Click Create

✅ Save:

AZURE_OPENAI_MODEL = gpt35

4.4 Get Endpoint and Key
Left menu → Keys and Endpoint

Copy:

Key

Endpoint (e.g., https://rag-openai.openai.azure.com/)

✅ Save:

AZURE_OPENAI_KEY

AZURE_OPENAI_ENDPOINT


