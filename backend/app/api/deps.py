import os

from elasticsearch import Elasticsearch
from typing import Generator


def get_es() -> Generator:
    return Elasticsearch(
        hosts=[os.environ.get("ELASTICSEARCH_URL")],
        http_auth=(os.environ.get("ELASTICSEARCH_USERNAME"),
                   os.environ.get("ELASTICSEARCH_PASSWORD"))
    )
