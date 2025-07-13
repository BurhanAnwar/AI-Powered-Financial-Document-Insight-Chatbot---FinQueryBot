from fastapi import FastAPI
from pydantic import BaseModel
from app.qa_chain import get_qa_chain

app = FastAPI()
qa = get_qa_chain()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    answer = qa.run(query.question)
    return {"answer": answer}
