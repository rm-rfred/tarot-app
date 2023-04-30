from fastapi import APIRouter

from api.endpoints import game

api_router = APIRouter()
api_router.include_router(game.router, prefix="/games", tags=["games"])
