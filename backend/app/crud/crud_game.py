
from elasticsearch import Elasticsearch
from fastapi import Depends

from api.deps import get_es


class CRUDGame():
    def __init__(self, nb_players: int) -> None:
        self.nb_players = nb_players

    def create(self, es: Elasticsearch = Depends(get_es)):
        es.index()
