def retrieve_docs(query: str) -> str:
    # Placeholder for FAISS/Pinecone retrieval
    if "login" in query.lower():
        return "According to the test plan, the login form must include both username and password fields."
    return "No relevant documentation found."
