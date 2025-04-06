from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))

def run_cypher_query(cypher):
    with driver.session() as session:
        result = session.run(cypher)
        return [dict(record) for record in result]
