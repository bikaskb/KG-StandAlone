from flask import Flask, request, render_template
from llm_cypher import get_cypher_query_from_nl
from query_handler import run_cypher_query
from llm_handler import convert_to_cypher

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        question = request.form["question"]

        # NEW: Convert NL question to Cypher query using LLaMA 3
        cypher = convert_to_cypher(question)

        # Run the generated Cypher query
        results = run_cypher_query(cypher)

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
