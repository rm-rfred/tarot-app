import os

from elasticsearch import Elasticsearch
from fastapi import Depends

from api.deps import get_es

ELASTICSEARCH_BASE_INDEX = os.environ.get("ELASTICSEARCH_BASE_INDEX")


def create_elastic_index(index: str, es: Elasticsearch = Depends(get_es)):
    if not es.indices.exists(index=f"{ELASTICSEARCH_BASE_INDEX}_{index}"):
        es.indices.create(index=f"{ELASTICSEARCH_BASE_INDEX}_{index}")
