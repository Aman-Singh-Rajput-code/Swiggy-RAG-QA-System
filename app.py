import os
from flask import Flask, render_template, request, jsonify
from rag_pipeline import SwiggyRAGPipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "data", "Swiggy_Annual_Report_FY_2023_24.pdf")

app = Flask(__name__)

rag = SwiggyRAGPipeline(PDF_PATH)
rag.build_vectorstore()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    question = data.get("question", "").strip()

    if not question:
        return jsonify({"answer": "Please enter a valid question.", "sources": []})

    answer, sources = rag.generate_answer(question)

    pages = list({src.metadata.get("page", "N/A") for src in sources})

    return jsonify({
        "answer": answer,
        "sources": pages
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
