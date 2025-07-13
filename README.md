# 💼 FinQueryBot – AI-Powered-Financial-Document-Insight-Chatbot

A production-ready AI-powered chatbot that lets you **ask questions from financial documents** like 10-Ks, tax returns, balance sheets, and contracts.

Built with 🔗 **LangChain**, 🤖 **OpenAI GPT-4o**, 📦 **FAISS**, ⚙️ **FastAPI**, and 💬 **Streamlit**.

---

## 📌 Features

- ✅ Upload **PDFs** like 10-Ks, balance sheets, contracts, etc.
- 💬 Ask natural language queries like:
  > “What was the net income in 2024?”
- 🤖 Powered by **GPT-4o** for better reasoning
- 🧠 Uses **FAISS** for semantic similarity search
- 📊 Embeddings with **OpenAI**
- 🎯 **Streamlit UI** + **FastAPI backend**

---

## 🧠 How It Works

1. PDF is uploaded and converted into text chunks
2. Text chunks are embedded using OpenAI embeddings
3. Stored in a FAISS vector database
4. When a user asks a question:
   - LangChain retrieves the most relevant chunks
   - Sends to GPT-4o for answering
   - Response is returned in chat

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

