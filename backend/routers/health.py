from fastapi import APIRouter
from datetime import datetime, timezone
from config import settings

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Health check endpoint for monitoring and deployment verification.
    Returns comprehensive status information about the API.
    """
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "environment": settings.environment,
        "api_version": "v1",
        "service": "real-estate-investment-api",
        "checks": {
            "api": "ok",
            # Future: Add database, external services, etc.
            # "database": "ok",
            # "cache": "ok",
        }
    }


@router.get("/health/live")
def liveness_check():
    """
    Liveness probe - indicates the service is running.
    Used by Kubernetes and container orchestration.
    """
    return {"status": "alive"}


@router.get("/health/ready")
def readiness_check():
    """
    Readiness probe - indicates the service is ready to accept traffic.
    Can be expanded to check database connections, external services, etc.
    """
    # Future: Add checks for database, cache, external APIs, etc.
    return {"status": "ready"}