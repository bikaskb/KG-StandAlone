from neo4j import GraphDatabase

# Update this with your local Neo4j credentials
URI = "bolt://localhost:7687"
USER = "neo4j"
PASSWORD = "12345678"

printer_data = {
    "HP LaserJet 1020": ["Print"],
    "Canon Pixma G3000": ["Print", "Scan", "Wireless"],
    "Epson EcoTank L3150": ["Print", "Scan", "Copy", "Wireless"],
}

def load_data():
    driver = GraphDatabase.driver(URI, auth=(USER, PASSWORD))
    with driver.session() as session:
        # Clear previous data (you can remove this line in production)
        session.run("MATCH (n) DETACH DELETE n")

        for printer, capabilities in printer_data.items():
            session.run("""
                MERGE (p:Printer {name: $printer})
            """, printer=printer)

            for cap in capabilities:
                session.run("""
                    MERGE (c:Capability {name: $cap})
                    MERGE (p:Printer {name: $printer})
                    MERGE (p)-[:HAS_CAPABILITY]->(c)
                """, printer=printer, cap=cap)

    print("Sample data loaded.")
    driver.close()


if __name__ == "__main__":
    load_data()
