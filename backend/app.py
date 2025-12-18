from fastapi import FastAPI
from pydantic import BaseModel
from retriever import retrieve

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    results = retrieve(req.query, k=10)
    return {"recommended_assessments": results}
