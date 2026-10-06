import os

from dotenv import load_dotenv


load_dotenv()

# Paths
DOCS_PATH = "docs"
PERSIST_DIRECTORY = "db/chroma_db"
COLLECTION_NAME = "pdf_documents"

CHUNK_SIZE = 800
CHUNK_OVERLAP = 0

EMBEDDING_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-4o-mini"
VISION_MODEL = "gpt-4o-mini"

RETRIEVAL_K = 3

# API key check - fail fast at startup, not mid-request
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in environment. Check your .env file.")
