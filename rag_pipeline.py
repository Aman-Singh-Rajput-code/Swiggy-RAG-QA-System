'''import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage'''

'''
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
'''

import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain.schema import SystemMessage, HumanMessage
from langchain_core.messages import SystemMessage, HumanMessage

#load_dotenv()
#load_dotenv()
load_dotenv(dotenv_path=".env", override=True)


class SwiggyRAGPipeline:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

        # Open-source embeddings
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        # Gemini LLM (hallucination-safe config)
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            max_output_tokens=512
        )

        self.vectorstore = None

    def load_and_split_pdf(self):
        loader = PyPDFLoader(self.pdf_path)
        documents = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        chunks = splitter.split_documents(documents)
        return chunks

    def build_vectorstore(self):
        chunks = self.load_and_split_pdf()
        self.vectorstore = FAISS.from_documents(
            chunks, self.embeddings
        )

    def retrieve_context(self, query: str, k: int = 4):

        retriever = self.vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": k}
        )
        return retriever.invoke(query)


    def generate_answer(self, query: str):
        docs = self.retrieve_context(query)

        if not docs:
            return "Answer not found in the provided document.", []

        context = "\n\n".join(
            [f"(Page {doc.metadata.get('page', 'N/A')}): {doc.page_content}" for doc in docs]
        )

        system_prompt = """
You are a strict document-based question answering assistant.

Rules:
- Answer ONLY from the provided context.
- The context comes from the Swiggy Annual Report FY 2023–24.
- If the answer is not explicitly present, say:
  "Answer not found in the provided document."
- Do NOT use external knowledge.
- Do NOT make assumptions.
"""

        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=f"Context:\n{context}\n\nQuestion:\n{query}")
        ]

        response = self.llm.invoke(messages)
        return response.content, docs
