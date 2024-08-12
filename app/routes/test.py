from fastapi import APIRouter

from app.repositories.test import test_db
from app.schemas.test import TestSchema

api = APIRouter()


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.get("/test-mongo", response_model=TestSchema | None)
async def test_mongo():
    return test_db()
