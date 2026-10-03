from fastapi import APIRouter

health_router = APIRouter()


@health_router.post("/health", tags=["health"])
def check_health():
    return {
        "status": "healthy"
    }

