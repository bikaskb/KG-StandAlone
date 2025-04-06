import requests
import re

def convert_to_cypher(question):
    prompt = f"""
You are a Cypher expert. Translate the following natural language query into a Cypher query that can be run on a Neo4j database of printers and their capabilities.

Only return the Cypher code and nothing else.

Question: {question}
Cypher:"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    raw_output = response.json()["response"]
    
    # Strip everything before the first "MATCH" or "RETURN" if needed
    match = re.search(r"(MATCH|RETURN|CALL|CREATE).*", raw_output, re.IGNORECASE | re.DOTALL)
    if match:
        cypher = match.group(0)
    else:
        cypher = raw_output  # fallback
    
    return cypher.strip()
