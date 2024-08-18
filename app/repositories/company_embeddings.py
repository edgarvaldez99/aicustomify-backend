from typing import List

from diskcache import Cache  # type: ignore
from langchain_community.vectorstores import FAISS
from pymongo.collection import Collection

from app.constants import CACHE_DIR, DEFAULT_LLM_NAME
from app.models import CompanyEmbeddingsDict
from app.schemas import CompanyEmbeddingsSchema

from .config import db
from .embeddings_model import get_embeddings_model

cache = Cache(CACHE_DIR)


def get_company_embeddings(
    company="company",
) -> CompanyEmbeddingsSchema | None:
    assert db is not None
    collection: Collection[CompanyEmbeddingsDict] = db.get_collection(
        name="company_embeddings"
    )
    result = collection.find_one({"company": company})
    if result is None:
        return None
    model = result["model"]
    cache_key = result["embeddings_cache_key"]
    embeddings = cache.get(cache_key)
    return CompanyEmbeddingsSchema(
        _id=result["_id"],
        company=result["company"],
        model=model,
        services=result["services"],
        embeddings={model: embeddings},
    )


def create_company_embeddings(
    company: str,
    services: List[str],
    model=DEFAULT_LLM_NAME,
) -> CompanyEmbeddingsSchema:
    assert db is not None
    collection: Collection[CompanyEmbeddingsDict] = db.get_collection(
        name="company_embeddings"
    )
    embeddings_model = get_embeddings_model(model)
    cache_key = f"{company}_{model}"
    services_embeddings: FAISS | None = cache.get(cache_key)
    if services_embeddings is None:
        if cache_key in cache:
            del cache[cache_key]
        services_embeddings = FAISS.from_texts(services, embeddings_model)
        cache.set(cache_key, services_embeddings)
    company_embeddings = CompanyEmbeddingsDict(
        company=company,
        model=model,
        services=services,
        embeddings_cache_key=cache_key,
    )
    result = collection.insert_one(company_embeddings)
    return CompanyEmbeddingsSchema(
        _id=result.inserted_id,
        company=company,
        model=model,
        services=services,
        embeddings={model: services_embeddings},
    )
