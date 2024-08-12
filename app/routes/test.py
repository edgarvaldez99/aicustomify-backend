from fastapi import APIRouter

api = APIRouter()


@api.get("/")
async def root():
    return {"message": "Hello World"}
