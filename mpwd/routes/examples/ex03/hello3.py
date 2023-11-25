from fastapi import APIRouter


router = APIRouter()


@router.get("/hi")
def hello3(who):
    """ Query Parameters """
    return f"Hello? {who}?"
