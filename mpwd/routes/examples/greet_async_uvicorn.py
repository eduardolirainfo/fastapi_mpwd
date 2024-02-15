"""
Example of a FastAPI route that uses async/await and uvicorn to run the server. 
"""
import asyncio

import uvicorn
from fastapi import APIRouter

router = APIRouter()


@router.get("/hi")
async def greet():
    """Greet the world."""
    await asyncio.sleep(1)
    return "Hello? World?"


if __name__ == "__main__":
    uvicorn.run("greet_async_uvicorn:app")
