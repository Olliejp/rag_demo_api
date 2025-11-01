from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import retrieval
import uvicorn

# Create FastAPI app
app = FastAPI()

# Configure CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rag-demo-frontend-r20o.onrender.com",
        "http://localhost:5173"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(retrieval.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Retrieval Demo API",
        "docs": "/docs",
        "health": "/retrieval/health"
    }


@app.get("/health")
async def health():
    """Global health check"""
    return {"status": "healthy"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
