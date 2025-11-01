from fastapi import APIRouter, HTTPException
from models.retrieval import RetrievalRequest, RetrievalResponse
from core.get_candidates_db import get_embedding_results

router = APIRouter(
    prefix="/retrieval",
    tags=["retrieval"]
)


@router.post("/search", response_model=RetrievalResponse)
async def search_embeddings(request: RetrievalRequest):
    """
    Call the core search function and return the results
    """
    try:
        # Call the core function
        results = get_embedding_results(
            user_query=request.user_query,
            match_count=request.match_count
        )

        return RetrievalResponse(
            query=request.user_query,
            match_count=request.match_count,
            results=results,
            total_results=len(results)
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing retrieval request: {str(e)}"
        )
