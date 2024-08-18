from app import app
from app.routes import api


app.include_router(api)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
