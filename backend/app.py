from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from retriever import retrieve

app = FastAPI()

# Allow frontend running on localhost:5500 to call this API
app.add_middleware(
    CORSMiddleware,
    # Allow all origins so deployed frontends (Vercel, etc.) can call the API
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str


@app.get("/")
def root():
    return {
        "message": "SHL Assessment Recommender API",
        "endpoints": ["/health", "/recommend", "/docs"],
    }

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/recommend")
def recommend(req: QueryRequest):
    results = retrieve(req.query, k=10)
    return {"recommended_assessments": results}
