from pymongo.collection import Collection

from app.models import TestDict
from app.schemas.test import TestSchema

from .config import db


def test_db() -> TestSchema | None:
    assert db is not None
    collection: Collection[TestDict] = db.get_collection("test")
    collection.insert_one(TestDict(test=1))
    result = collection.find_one({"test": 1})
    return TestSchema(**result) if result else None
