import os

from fastapi import APIRouter

router = APIRouter()


@router.post("/", status_code=201)
def create_game(index: str):
    pass
