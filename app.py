from flask import Flask, request, render_template
from graph.agent_graph import graph

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            state = {"query": query}
            result = graph.invoke(state)
            report = result.get("report", "No report generated.")
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)