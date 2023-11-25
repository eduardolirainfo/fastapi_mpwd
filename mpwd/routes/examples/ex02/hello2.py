from fastapi import APIRouter


router = APIRouter()


@router.get("/hi/{who}")
def hello2(who):
    """URL Path Parameter"""
    return f"Hello? {who}?"
