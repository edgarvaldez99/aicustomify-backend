from fastapi import APIRouter, Form

from app.services import search_text_in_service

api = APIRouter()


@api.post("/", response_model=str | None)
async def ask_about_service(search_text: str = Form(...)):
    return search_text_in_service(search_text)
