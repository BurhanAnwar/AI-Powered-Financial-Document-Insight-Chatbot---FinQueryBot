from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import sys
import os

def ingest(file_path):
    print(f"Loading file: {file_path}")
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents from PDF")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")

    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.from_documents(chunks, embeddings)

    # Save vectorstore using FAISS method (not pickle)
    vectorstore.save_local("faiss_store")
    print("[✓] FAISS vector store created and saved.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ingest.py <pdf-file-path>")
    else:
        ingest(sys.argv[1])
