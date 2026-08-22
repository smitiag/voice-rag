from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(
    title="Voice RAG API",
    version="1.0.0"
)

app.include_router(router)


@app.get("/")
def root():
    return {
        "message": "Voice RAG API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }