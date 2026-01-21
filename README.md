# Swiggy Annual Report RAG QA System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) based Question Answering system
using the Swiggy Annual Report FY 2023–24.

The system answers questions strictly based on the report content and prevents hallucination.

## Architecture
1. PDF Loader (PyPDFLoader)
2. Text Chunking (RecursiveCharacterTextSplitter)
3. Embeddings (Sentence Transformers)
4. Vector Store (FAISS)
5. Retriever (Similarity Search)
6. LLM (OpenAI, temperature=0)
7. CLI Interface

## LLM Used
Google Gemini (`gemini-1.5-flash`) via LangChain

Why Gemini:
- Strong reasoning
- Low latency
- Deterministic outputs with temperature=0
- Production-ready API


## Data Source
Swiggy Annual Report FY 2023–24  
Public Link: https://www.swiggy.com/about-us/

## Hallucination Prevention
- Temperature set to 0
- Explicit system instructions
- Only retrieved context passed to LLM
- No external data usage
- Refusal when answer is not present

## How to Run

```bash
pip install -r requirements.txt
export OPENAI_API_KEY=your_api_key
python app.py
