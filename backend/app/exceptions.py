"""
Custom exception handlers for the API
"""
from fastapi import Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder


async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Custom handler for validation errors
    Returns a clean error response for invalid request data
    """
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={
            "detail": jsonable_encoder(exc.errors()),
            "message": "Validation error",
        },
    )


async def general_exception_handler(request: Request, exc: Exception):
    """
    General exception handler for unhandled errors
    """
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "detail": "Internal server error",
            "message": str(exc) if __debug__ else "An error occurred",
        },
    )

