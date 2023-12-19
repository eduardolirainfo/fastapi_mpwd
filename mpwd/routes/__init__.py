from fastapi import APIRouter
from .examples.hello import router as hello
from .examples.tag import router as tag


main_router = APIRouter()
main_router.include_router(hello, tags=["Hello"])
main_router.include_router(tag, prefix="/tag", tags=["Tag"])
