from app import app
from app.routes import api


app.include_router(api)
