# Pydantic schemas for request/response validation
from pydantic import BaseModel
from typing import List, Optional

class RecommendationRequest(BaseModel):
    job_description: str
    num_recommendations: Optional[int] = 5

class Assessment(BaseModel):
    id: str
    name: str
    description: str
    score: float

class RecommendationResponse(BaseModel):
    assessments: List[Assessment]
