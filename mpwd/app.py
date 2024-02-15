""" FastAPI app """
from fastapi import FastAPI

from .routes import main_router

app = FastAPI(
    title="mpwd",
    version="0.1.0",
    description="mpwd",
)

# uvicorn mpwd.app:app --reload
app.include_router(main_router)
