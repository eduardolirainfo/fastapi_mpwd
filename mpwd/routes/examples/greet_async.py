""" Example of an async route. """
import asyncio

from fastapi import APIRouter

router = APIRouter()


@router.get("/hi")
async def greet():
    """Greet the world."""
    await asyncio.sleep(1)
    return "Hello? World?"
