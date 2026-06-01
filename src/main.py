from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.routers import ingestion

app = FastAPI(
    title="Organizational Cognition Runtime",
    description="Cognitive operating system for organizations",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingestion.router)

@app.get("/health")
async def health():
    return {"status": "ok", "service": "ocr-api", "version": "0.1.0"}

@app.get("/")
async def root():
    return {
        "service": "Organizational Cognition Runtime",
        "docs": "/docs",
        "health": "/health",
    }
