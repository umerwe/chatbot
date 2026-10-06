from langchain_core.messages import HumanMessage, SystemMessage
from app.core import config
from app.core.models import llm_model
from app.core.vectorstore import db


def build_prompt(query: str, relevant_docs):
    document_text = "\n".join([f"- {doc.page_content}" for doc in relevant_docs])
    return f"""Based on the following documents, please answer this question: {query}

Documents:
{document_text}

Please provide a clear, helpful answer using only the information from these documents. If you can't answer based on the documents, say so."""


async def retrieval(query: str):
    # Async Vector Search
    retriever = db.as_retriever(search_kwargs={"k": config.RETRIEVAL_K})
    relevant_docs = await retriever.ainvoke(query)
    
    combined_input = build_prompt(query, relevant_docs)
    messages = [
        SystemMessage(content="You are a helpful assistant"),
        HumanMessage(content=combined_input),
    ]

    result = await llm_model.ainvoke(messages)
    return {
        "answer": result.content,
        "chunks_length": len(relevant_docs),
    }