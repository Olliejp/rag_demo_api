from pydantic import BaseModel, Field
from typing import List, Any


class RetrievalRequest(BaseModel):
    """Request model for embedding retrieval endpoint"""
    user_query: str = Field(..., description="The query text to search for")
    match_count: int = Field(default=5, ge=1, le=100, description="Number of matches to return")


class RetrievalResponse(BaseModel):
    """Response model for embedding retrieval endpoint"""
    query: str = Field(..., description="The original user query")
    match_count: int = Field(..., description="Number of matches requested")
    results: List[Any] = Field(..., description="List of matching results from database")
    total_results: int = Field(..., description="Total number of results returned")
