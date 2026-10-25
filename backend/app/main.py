from fastapi import FastAPI

from .api.routes import router

app = FastAPI(title="Life Stats API", version="0.1.0")
app.include_router(router, prefix="/api")
