""" Starlette Hello World Example """
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def greeting(request):
    """Return a greeting question mark"""
    return JSONResponse("Hello? World?")


app = Starlette(
    debug=True,
    routes=[
        Route("/hi", greeting),
    ],
)
