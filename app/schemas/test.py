from pydantic import BaseModel

from app.models import ObjectId


class TestSchema(BaseModel):
    _id: ObjectId | None
    test: int
