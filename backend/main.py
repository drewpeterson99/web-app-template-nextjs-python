# run backend server with: python main.py
# or: uvicorn main:app --reload --host 127.0.0.1 --port 8000

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from config import settings
from api.v1.router import api_router
from app.exceptions import (
    validation_exception_handler,
    general_exception_handler,
)
import uvicorn

app = FastAPI(
    title="Full-Stack App API",
    description="API for template full-stack web application",
    version="1.0.0",
)

# Add exception handlers
app.add_exception_handler(RequestValidationError, validation_exception_handler)
app.add_exception_handler(Exception, general_exception_handler)

# Configure CORS to allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Template Web Application API"}

# Simple health check at root (for load balancers/monitoring tools)
@app.get("/health")
def root_health_check():
    """Simple health check at root level for infrastructure tools"""
    return {"status": "healthy"}

# Include API v1 router (all business logic should be versioned)
app.include_router(api_router, prefix=settings.api_v1_prefix)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.host,
        port=settings.port,
        reload=True
    )
