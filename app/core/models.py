from langchain_openai import ChatOpenAI, OpenAIEmbeddings

from app.core import config


embedding_model = OpenAIEmbeddings(model=config.EMBEDDING_MODEL)
llm_model = ChatOpenAI(model=config.CHAT_MODEL)
vision_model = ChatOpenAI(model=config.VISION_MODEL, temperature=0)