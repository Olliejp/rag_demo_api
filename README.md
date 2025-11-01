# RAG Demo Backend

FastAPI backend for a finance-focused arXiv paper search engine using semantic search.

## Directory Structure

```
backend/
├── main.py                          # FastAPI app entry point, CORS config, and route registration
├── requirements.txt                 # Python dependencies
│
├── core/                           # Core lin scripts
│   ├── __init__.py
│   └── get_candidates_db.py        # Embedding generation and vector similarity search on DB
│
├── routes/                         # API route handlers
│   ├── __init__.py
│   └── retrieval.py                # /retrieval/search endpoint
│
├── models/                         # Pydantic models for request/response validation
│   ├── __init__.py
│   └── retrieval.py                # RetrievalRequest and RetrievalResponse schemas
│
└── utils/                          # Utility functions and configuration
    ├── __init__.py
    └── config_.py                  # Application configuration (embedding model settings)
```

## Architecture

### Request Flow

1. **Client** sends POST request to `/retrieval/search` with user query
2. **Route Handler** (`routes/retrieval.py`) validates request via Pydantic models
3. **Core Logic** (`core/get_candidates_db.py`):
   - Converts user query to 1024-dim embedding using Voyage AI
   - Queries Supabase RPC function for cosine similarity matches
   - Returns top N most relevant papers
4. **Response** returned to client with paper metadata

### Key Components

- **Embedding Model**: Voyage AI (`voyage-3.5-lite`, 1024 dimensions)
- **Vector Database**: Supabase with pgvector extension
- **API Framework**: FastAPI

## Environment Variables

Required in `.env`:
```
VOYAGE_AI_KEY=your_voyage_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_SERVICE_ROLE_KEY=your_supabase_service_key
```

## Deployment

Deployed on Render with the following configuration:
- **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
- **Environment Variables**: Set in Render dashboard
- **URL**: https://rag-demo-api.onrender.com

## API Endpoints

### POST /retrieval/search

Search for relevant arXiv papers using semantic similarity.

**Request Body:**
```json
{
  "user_query": "machine learning for portfolio optimization",
  "match_count": 5
}
```

**Response:**
```json
{
  "query": "machine learning for portfolio optimization",
  "match_count": 5,
  "total_results": 5,
  "results": [
    {
      "title": "Paper Title",
      "submission_date": "2024-01-15",
      "primary_subject": "q-fin.PM",
      "doi": "https://arxiv.org/abs/2401.12345",
      "abstract": "Paper abstract..."
    }
  ]
}
```
