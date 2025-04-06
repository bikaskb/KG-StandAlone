import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"

# System prompt template
PROMPT_TEMPLATE = """You are a Cypher expert for Neo4j graph databases.
Translate the user's natural language question into a Cypher query.
Assume a graph with Printer and Capability nodes and relationships like (:Printer)-[:HAS_CAPABILITY]->(:Capability).

User question: "{question}"

Cypher query:
"""

def get_cypher_query_from_nl(question):
    prompt = PROMPT_TEMPLATE.format(question=question)
    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    })
    response.raise_for_status()
    result = response.json()
    return result["response"].strip()
