from fastapi import APIRouter, Body


router = APIRouter()


@router.post("/hi")
def greet(who: str = Body(embed=True)):
    """Body Parameter"""
    return f"Hello? {who}?"
