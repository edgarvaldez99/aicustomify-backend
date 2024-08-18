from fastapi import APIRouter

from . import search_text_in_test_service
from . import test

api = APIRouter()

api.include_router(
    search_text_in_test_service.api,
    prefix="/search",
    tags=["search"],
)
api.include_router(test.api, prefix="/test", tags=["test"])
