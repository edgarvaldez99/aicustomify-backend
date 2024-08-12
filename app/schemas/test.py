from typing_extensions import TypedDict, NotRequired

from pydantic import BaseModel

from .objectid import ObjectId


class TestSchemaDict(TypedDict):
    _id: NotRequired[ObjectId]
    test: int


class TestSchema(BaseModel):
    _id: ObjectId | None
    test: int
