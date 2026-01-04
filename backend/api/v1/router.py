from fastapi import APIRouter
from routers import health, properties

api_router = APIRouter()

# Include all routers
api_router.include_router(health.router, tags=["health"])
api_router.include_router(properties.router, tags=["properties"])

