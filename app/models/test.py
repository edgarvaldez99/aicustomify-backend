from typing_extensions import TypedDict, NotRequired

from .objectid import ObjectId


class TestDict(TypedDict):
    _id: NotRequired[ObjectId]
    test: int
