from langchain_chroma import Chroma

from app.core.models import embedding_model
from app.core import config


db = Chroma(
    persist_directory=config.PERSIST_DIRECTORY,
    embedding_function=embedding_model,
    collection_name=config.COLLECTION_NAME,
    collection_metadata={"hnsw:space": "cosine"},
)
