from fastapi import APIRouter

from app.api.endpoints import game

api_router = APIRouter()
api_router.include_router(game.router, prefix="/games", tags=["games"])
