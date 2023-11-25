from fastapi import APIRouter
# from .examples.ex01.hello import router as example1
# from .examples.ex02.hello2 import router as example2
# from .examples.ex03.hello3 import router as example3
from .examples.ex04.hello4 import router as example4


main_router = APIRouter()
# main_router.include_router(example1)
# main_router.include_router(example2)
# main_router.include_router(example3)
main_router.include_router(example4)
