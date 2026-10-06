from app.loaders.document_loader import partition_document
from unstructured.chunking.title import chunk_by_title
from app.core.summarizer import summarise_chunks
from app.core import config
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

# Test with your PDF file
file_path = "./docs/test-4-pages.pdf"  # Change this to your PDF path
elements = partition_document(file_path)

print(f"✅ Created {len(elements)} elements")

def create_chunks_by_title(elements):
    
    chunks = chunk_by_title(
        elements,                      # The parsed PDF elements from previous step
        max_characters=3000,           # Hard limit - never exceed 3000 characters per chunk
        new_after_n_chars=2400,        # Try to start a new chunk after 2400 characters
        combine_text_under_n_chars=500 # Merge tiny chunks under 500 chars with neighbors
    )

    return chunks


# Create chunks
chunks = create_chunks_by_title(elements)

# Summarize chunks
processed_chunks = summarise_chunks(chunks)

# --- Chroma mein save karo ---
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

vector_store = Chroma.from_documents(
    documents=processed_chunks,
    embedding=embeddings,
    persist_directory=config.PERSIST_DIRECTORY,
    collection_name=config.COLLECTION_NAME
)

print(f"✅ {len(processed_chunks)} documents Chroma mein save ho gaye")

