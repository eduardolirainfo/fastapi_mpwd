import datetime
from fastapi import APIRouter
from mpwd.model.tag import TagIn, Tag, TagOut
import mpwd.service.tag as service

router = APIRouter()


@router.post("/")
def create(tag_in: TagIn) -> TagIn:
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.datetime.now(), secret="shhhh")
    service.create(tag)
    return tag_in


@router.get("/{tag_str}", response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    tag: Tag = service.get(tag_str)
    return tag
