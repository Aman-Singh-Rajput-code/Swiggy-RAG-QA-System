📘 Swiggy Annual Report RAG-Based Question Answering System
📌 Project Overview

This project implements a Retrieval-Augmented Generation (RAG) based Question Answering system using the Swiggy Annual Report (FY 2023–24).

The system answers user queries strictly based on the content of the annual report PDF and is explicitly designed to prevent hallucinations.
If the requested information is not present in the document, the system clearly responds with:

“Answer not found in the provided document.”

This project demonstrates:

Document ingestion

Vector-based retrieval

LLM grounding

Hallucination prevention

End-to-end ML system design

🎯 Objective

Build a document-grounded QA system

Ensure zero hallucination

Use RAG architecture with modern ML tooling

Keep the implementation simple, modular, and production-readable

🧠 Architecture Overview
Swiggy Annual Report (PDF)
        ↓
PDF Loader (PyPDF)
        ↓
Text Chunking + Metadata
        ↓
Embedding Model (Sentence Transformers)
        ↓
Vector Store (FAISS)
        ↓
Retriever (Top-k similarity search)
        ↓
Gemini LLM (temperature = 0)
        ↓
Grounded Answer + Source Pages

🔧 Technology Stack
Component	Tool
Language	Python 3.10
Backend	Flask
RAG Framework	LangChain
LLM	Google Gemini
Embeddings	sentence-transformers/all-MiniLM-L6-v2
Vector DB	FAISS
PDF Parsing	PyPDF
Frontend	HTML, CSS, JavaScript
Version Control	Git & GitHub
📂 Project Structure
Swiggy-RAG-QA-System/
│
├── app.py                  # Flask backend + API
├── rag_pipeline.py         # RAG logic (load, embed, retrieve, generate)
├── requirements.txt        # Python dependencies
├── runtime.txt             # Python version (3.10.12)
├── .gitignore              # Git ignore rules
├── README.md               # Project documentation
│
├── data/
│   └── Swiggy_Annual_Report_FY_2023_24.pdf
│
├── templates/
│   └── index.html          # Frontend UI
│
└── static/
    ├── style.css
    └── script.js

📄 Dataset

Swiggy Annual Report FY 2023–24

Publicly available corporate document

Source: https://www.swiggy.com/about-us/

The report contains:

Business overview

Operations

Financial information

Governance & compliance

⚠️ All answers are strictly grounded in this document only.

🧩 RAG Implementation Details
1️⃣ Document Loading

PDF loaded using PyPDFLoader

Page numbers preserved as metadata

2️⃣ Text Chunking

Recursive character splitting

Overlapping chunks for contextual continuity

3️⃣ Embeddings

Open-source sentence transformer

Lightweight and efficient for local FAISS usage

4️⃣ Vector Store

FAISS used for fast similarity search

In-memory index built at application startup

5️⃣ Retrieval

Top-k similarity retrieval

Only retrieved chunks passed to the LLM

6️⃣ Answer Generation

Gemini LLM used as a reasoning engine only

No external knowledge access

🚫 Hallucination Prevention Techniques

The system prevents hallucinations using multiple safeguards:

Temperature set to 0

Explicit system instruction:

“Answer only from the provided context. If not present, say ‘Answer not found in the provided document.’”

Only retrieved document chunks passed to the LLM

No internet access

No memory across queries

Refusal for future, comparative, or speculative questions

🖥️ How to Run Locally
1️⃣ Clone the Repository
git clone https://github.com/Aman-Singh-Rajput-code/Swiggy-RAG-QA-System.git
cd Swiggy-RAG-QA-System

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Gemini API Key

Create a .env file (not committed confirm):

GOOGLE_API_KEY=your_gemini_api_key


Or set it as an environment variable.

5️⃣ Run the Application
python app.py


Open browser at:

http://localhost:5000

🧪 Example Questions for Testing
✅ In-Scope Questions
What type of company is Swiggy described as?
What investments or expenditures are mentioned in FY 2023–24?
What business segments does Swiggy operate in?

🚫 Hallucination Test Questions
What is Swiggy’s stock price in 2024?
How does Swiggy compare financially to Zomato?
What are Swiggy’s future plans for 2026?


Expected response:

Answer not found in the provided document.

🔐 Security & Best Practices

API keys are not hardcoded

.env is excluded via .gitignore

Sensitive files are never committed

Clean dependency management via requirements.txt

🧠 Key Learnings Demonstrated

Practical RAG system design

Handling LLM hallucination risks

Vector search & semantic retrieval

Debugging real-world ML deployment issues

Clean Git & project structure practices

📌 Note on Deployment

Deployment is intentionally excluded from this README to keep the focus on:

Core ML system design

RAG correctness

Hallucination safety

Local reproducibility

👤 Author

Aman Singh Rajput
GitHub: https://github.com/Aman-Singh-Rajput-code

✅ Final Remarks

This project demonstrates an end-to-end, production-style RAG pipeline that prioritizes correctness, safety, and clarity — exactly what is expected from a modern ML engineering workflow.
