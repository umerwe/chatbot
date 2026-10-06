from app.pipelines.retrieval import retrieval

def get_chat_response(query: str):
    return retrieval(query)
