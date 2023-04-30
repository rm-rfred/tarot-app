import os

from elasticsearch import Elasticsearch
from fastapi import APIRouter, Depends

from api.deps import get_es
from utils.es_utils import create_elastic_index

router = APIRouter()


@router.post("/", status_code=201)
def create_game(index: str):
    es = Elasticsearch(
        hosts=["https://171.17.0.1:9200"],
        http_auth=("admin", "admin"),
        verify_certs=None
    )
    return es.indices.create(index="tarot_games")
