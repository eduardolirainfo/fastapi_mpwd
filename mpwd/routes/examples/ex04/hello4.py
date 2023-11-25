from fastapi import APIRouter, Body


router = APIRouter()


@router.post("/hi")
def hello4(who: str = Body(embed=True)):
    return f"Hello? {who}?"

