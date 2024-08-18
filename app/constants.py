import os

from decouple import config as env  # type: ignore

APP_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_LLM_NAME = (
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"  # noqa: E501
)
OPENAI_KEY = str(env("OPENAI_KEY"))
ROOT_DIR = os.path.join(APP_DIR, "..")
CACHE_DIR = os.path.join(ROOT_DIR, "cache")
