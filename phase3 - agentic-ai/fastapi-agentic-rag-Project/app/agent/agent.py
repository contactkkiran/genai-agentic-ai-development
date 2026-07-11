"""
agent.py

Responsibility:
    Agent Orchestration Layer

Flow:

FastAPI
   |
   v
run_agent()
   |
   v
LangChain Agent
   |
   +--> PDFRetriever Tool
             |
             v
        Chroma Vector DB
             |
             v
        Relevant PDF Chunks
             |
             v
        GPT Response
"""

# =====================================================
# STEP 1:
# Import required LangChain components
# =====================================================

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

from app.rag.rag import build_vectorstore

# =====================================================
# STEP 2:
# Load existing Chroma Vector Database
#
# PDF
#  |
#  v
# Chunks
#  |
#  v
# Embeddings
#  |
#  v
# Chroma DB
#
# build_vectorstore() connects to Chroma
# =====================================================

vectorstore = build_vectorstore()


# =====================================================
# STEP 3:
# Create Agent Tool
#
# @tool converts Python function
#
# Normal Function
#        |
#        v
# LangChain Agent Tool
#
# Agent can call this automatically
# =====================================================


@tool
def PDFRetriever(query: str) -> str:
    """
    Searches PDF knowledge base
    and returns relevant chunks.
    """

    # -------------------------------------------------
    # STEP 3.1
    #
    # Convert user question into vector search
    #
    # Example:
    # "What is leave policy?"
    #
    #        |
    #        v
    #
    # Chroma similarity search
    #
    #        |
    #        v
    #
    # Matching PDF chunks
    # -------------------------------------------------

    docs = vectorstore.similarity_search(query)

    # -------------------------------------------------
    # STEP 3.2
    #
    # Convert list of Documents
    #
    # [
    #   Document(page_content="chunk1"),
    #   Document(page_content="chunk2")
    # ]
    #
    # into plain text context
    # -------------------------------------------------

    context = "\n\n".join(doc.page_content for doc in docs)

    return context


# =====================================================
# STEP 4:
# Create LLM Brain
#
# temperature=0
# gives consistent enterprise answers
# =====================================================

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)


# =====================================================
# STEP 5:
# Create Agent
#
# Agent receives:
#
# Brain  -> GPT Model
# Tools  -> PDFRetriever
#
# It decides:
#
# Answer myself?
#        OR
# Use PDFRetriever?
#
# (Replacement for old initialize_agent)
# =====================================================

agent = create_agent(model=llm, tools=[PDFRetriever])


# =====================================================
# STEP 6:
# Agent Execution Function
#
# FastAPI calls this method
# =====================================================


def run_agent(query: str):

    # -------------------------------------------------
    # Example:
    #
    # query =
    # "Explain onboarding process"
    #
    # Agent starts reasoning:
    #
    # Need PDF?
    #    |
    #    v
    # Call PDFRetriever
    #    |
    #    v
    # Get Chroma chunks
    #    |
    #    v
    # Generate answer
    # -------------------------------------------------

    result = agent.invoke({"messages": [{"role": "user", "content": query}]})

    # -------------------------------------------------
    # Return only final AI answer
    # -------------------------------------------------

    return result["messages"][-1].content
