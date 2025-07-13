import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def get_qa_chain():
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    faiss_path = os.path.join(base_dir, "faiss_store")
    
    vectorstore = FAISS.load_local(
        faiss_path,
        embeddings,
        allow_dangerous_deserialization=True
    )
    
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI(temperature=0)
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    
    return qa_chain
