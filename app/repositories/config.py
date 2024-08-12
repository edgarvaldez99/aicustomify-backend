from decouple import config as env  # type: ignore
from pymongo import MongoClient


MONGO_USER = str(env("MONGO_USER", "user"))
MONGO_PASS = str(env("MONGO_PASS", "pass"))
MONGO_HOST = str(env("MONGO_HOST", "localhost"))
MONGO_NAME = str(env("MONGO_NAME", "database"))
MONGO_DATABASE_URI = f"mongodb://{MONGO_USER}:{MONGO_PASS}@{MONGO_HOST}"

client = MongoClient(MONGO_DATABASE_URI)  # type: ignore

db = client.get_database(MONGO_NAME)
