from pymongo.collection import Collection

from app.schemas.test import TestSchema, TestSchemaDict

from .config import db


def test_db() -> TestSchema | None:
    assert db is not None
    collection: Collection[TestSchemaDict] = db.get_collection("test")
    collection.insert_one(TestSchemaDict(test=1))
    result = collection.find_one({"test": 1})
    return TestSchema(**result) if result else None
