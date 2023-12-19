from fastapi import APIRouter, Body, Header, Response


router = APIRouter()


# ex01
@router.get("/hi")
def hello():
    """Return a greeting question mark"""
    return "Hello? World?"


# ex02
@router.get("/hi/02/{who}")
def hello2(who):
    """URL Path Parameter"""
    return f"Hello? {who}?"


# ex03
@router.get("/hi/03")
def hello3(who):
    """ Query Parameters """
    return f"Hello? {who}?"


# ex04
@router.post("/hi/04")
def hello4(who: str = Body(embed=True)):
    """ Request Body """
    return f"Hello? {who}?"


# ex05
@router.post("/hi/05")
def hello5(who: str = Header()):
    """ Header """
    return f"Hello? {who}?"


# ex06
@router.post("/agent")
def get_agent(user_agent: str = Header()):
    """ User-Agent """
    return user_agent


# ex07
@router.get("/happy")
def happy(status_code=200):
    """ Status Code """
    return ":)"


# ex08
@router.get("/header/{name}/{value}")
def header(name: str, value: str, response: Response):
    """ Response Headers """
    response.headers[name] = value
    return "normal body"
