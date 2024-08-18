from diskcache import Cache  # type: ignore
from langchain_huggingface import HuggingFaceEmbeddings

from app.constants import CACHE_DIR, DEFAULT_LLM_NAME

cache = Cache(CACHE_DIR)


def get_embeddings_model(model=DEFAULT_LLM_NAME) -> HuggingFaceEmbeddings:
    cache_key = f"embeddings_model_{model}"
    embeddings: HuggingFaceEmbeddings | None = cache.get(cache_key)

    if embeddings is None:
        embeddings = HuggingFaceEmbeddings(model_name=model)
        cache.set(cache_key, embeddings)

    return embeddings
