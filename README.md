# 💼 FinQueryBot – AI-Powered-Financial-Document-Insight-Chatbot

A production-ready **Retrieval-Augmented Generation (RAG)** system that lets you chat with your financial documents — **analyze 10-Ks, tax returns, contracts, balance sheets** with natural language queries.

Built with 🔗 **LangChain**, 🤖 **OpenAI GPT-4o**, 📦 **FAISS**, ⚙️ **FastAPI**, and 💬 **Streamlit**.

---

## 🚀 Features

- 🧠 **RAG pipeline** with LangChain + FAISS
- 🤖 Answers powered by **OpenAI GPT (ChatGPT / GPT-4o)**
- 📄 Upload and embed **PDF financial documents**
- 🔍 Ask questions like “What was the cash flow in 2023?”
- ⚙️ **FastAPI** backend for inference
- 💬 **Streamlit** frontend for seamless interaction




---

## 🧠 How It Works
PDF is uploaded manually and processed via `ingest.py`
-- The document is:
- Loaded using PyPDFLoader
- Split into manageable chunks using RecursiveCharacterTextSplitter
- Converted into vector embeddings using OpenAIEmbeddings
- FAISS vector store is created locally and saved in the project as faiss_store/
- When a user asks a question through the Streamlit UI:
- The question is sent to the FastAPI backend (/ask endpoint)
- LangChain’s RetrievalQA retrieves the most relevant chunks using FAISS retriever
- The retrieved context is sent to OpenAI’s GPT-4o (via ChatOpenAI)
- A precise answer is generated and returned in the chat interface

---

## 🗂️ Project Structure
```bash
financial_querybot/
├── app/
│ ├── main.py ← FastAPI app
│ ├── qa_chain.py ← LangChain RAG setup
│ ├── ingest.py ← Load & embed docs
│ └── config.py ← API keys & DB info
├── run_ui.py ← Streamlit UI
├── requirements.txt
└── .env ← Your OpenAI key here
```

## 📄 Example Queries
- What was the total revenue in 2024?
- Summarize the cash flow section.
- Who signed the contract?
- List major expenses this year.

## 🏢 Ideal For
- Auditing firms
- CFOs & finance teams
- Investors & analysts
- Financial consultants

## Author
- M Burhan ud din

