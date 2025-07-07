# File type handling, extension check
ALLOWED_EXTENSIONS = {'.pdf', '.docx', '.txt', '.html', '.pptx', '.xlsx', '.csv'}

def allowed_file(filename: str) -> bool:
    return any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS)

def chunk_text(text: str, chunk_size: int = 500) -> list:
    # Splits long text into smaller chunks (useful for embeddings)
    words = text.split()
    return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]
