""" Routes for the API. """
from fastapi import APIRouter

from .examples.greet_async import router as greet_async
from .examples.greet_async_uvicorn import router as greet_async_uvicorn
from .examples.hello import router as hello
from .examples.tag import router as tag

main_router = APIRouter()
main_router.include_router(hello, tags=["Hello"])
main_router.include_router(tag, prefix="/tag", tags=["Tag"])
main_router.include_router(greet_async, prefix="/async", tags=["Async"])
main_router.include_router(
    greet_async_uvicorn, prefix="/async/uvicorn", tags=["Async Uvicorn"]
)
