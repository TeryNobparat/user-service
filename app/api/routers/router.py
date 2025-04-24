from fastapi import APIRouter
from app.api.routers.user.user import router as user_router
from app.api.routers.user.auth import router as auth_router
api_router = APIRouter()

api_router.include_router(user_router, prefix="/user", tags=["Users"])
api_router.include_router(auth_router, prefix="/authentication", tags=["Authentication"])

