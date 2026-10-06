from langchain_chroma import Chroma
from langchain_text_splitters import CharacterTextSplitter

from app.core import config
from app.core.models import embedding_model
from app.loaders.document_loader import load_docs


def chunking(documents):
    text_splitter = CharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
    )

    chunks = text_splitter.split_documents(documents)

    return chunks


def save_chunks_in_db(chunks):
    db = Chroma.from_documents(
        persist_directory=config.PERSIST_DIRECTORY,
        documents=chunks,
        embedding=embedding_model,
        collection_name=config.COLLECTION_NAME,
        collection_metadata={"hnsw:space": "cosine"},
    )

    return db


def run_ingestion():
    # Load the docs and returns text
    documents = load_docs()
    # Chunk the text and returns chunked text
    chunks = chunking(documents)
    # Save the chunks inside db
    save_chunks_in_db(chunks)
