from fastapi import APIRouter

from . import test

api = APIRouter()

api.include_router(test.api, prefix="/test", tags=["test"])
