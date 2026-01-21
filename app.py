'''from rag_pipeline import SwiggyRAGPipeline

PDF_PATH = "data/Swiggy_Annual_Report_FY_2023_24.pdf"


def main():
    rag = SwiggyRAGPipeline(PDF_PATH)
    print("Building vector store...")
    rag.build_vectorstore()
    print("Ready! Ask questions about Swiggy Annual Report.\n")

    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer, sources = rag.generate_answer(query)

        print("\nAnswer:")
        print(answer)

        print("\nSources:")
        for src in sources:
            print(f"- Page {src.metadata.get('page', 'N/A')}")
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()
'''

'''
import os
from rag_pipeline import SwiggyRAGPipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "data", "Swiggy_Annual_Report_FY_2023_24.pdf")


def main():
    rag = SwiggyRAGPipeline(PDF_PATH)
    print("Building vector store...")
    rag.build_vectorstore()
    print("Ready! Ask questions about Swiggy Annual Report.\n")

    while True:
        query = input("Ask a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        answer, sources = rag.generate_answer(query)

        print("\nAnswer:")
        print(answer)

        print("\nSources:")
        for src in sources:
            print(f"- Page {src.metadata.get('page', 'N/A')}")
        print("\n" + "-" * 50)


if __name__ == "__main__":
    main()
'''

import os
from flask import Flask, render_template, request, jsonify
from rag_pipeline import SwiggyRAGPipeline

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PATH = os.path.join(BASE_DIR, "data", "Swiggy_Annual_Report_FY_2023_24.pdf")

app = Flask(__name__)

# Initialize RAG once (important for performance)
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
