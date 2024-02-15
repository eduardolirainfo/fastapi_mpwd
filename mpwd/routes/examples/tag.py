"""
Tag routes
"""
import datetime

from fastapi import APIRouter

import mpwd.service.tag as service
from mpwd.model.tag import Tag, TagIn, TagOut

router = APIRouter()


@router.post("/")
def create(tag_in: TagIn) -> TagIn:
    """
    Create a tag
    """
    tag: Tag = Tag(tag=tag_in.tag, created=datetime.datetime.now(), secret="shhhh")
    service.create(tag)
    return tag_in


@router.get("/{tag_str}", response_model=TagOut)
def get_one(tag_str: str) -> TagOut:
    """
    Get a tag
    """
    tag: Tag = service.get(tag_str)
    return tag
