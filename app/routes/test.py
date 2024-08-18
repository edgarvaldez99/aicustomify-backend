from fastapi import APIRouter

from app.repositories import test_db
from app.schemas import TestSchema

api = APIRouter()


@api.get("/")
async def root():
    return {"message": "Hello World"}


@api.get("/test-mongo", response_model=TestSchema | None)
async def test_mongo():
    return test_db()
