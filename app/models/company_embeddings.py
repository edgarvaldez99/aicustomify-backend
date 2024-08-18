from typing_extensions import List, NotRequired, TypedDict

from .objectid import ObjectId


class CompanyEmbeddingsDict(TypedDict):
    _id: NotRequired[ObjectId]
    company: str
    model: str
    services: List[str]
    embeddings_cache_key: str
