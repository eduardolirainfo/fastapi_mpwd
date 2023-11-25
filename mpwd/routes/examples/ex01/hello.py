from fastapi import APIRouter


router = APIRouter()


@router.get("/hi")
def hello():
    """Return a greeting question mark"""
    return "Hello? World?"
