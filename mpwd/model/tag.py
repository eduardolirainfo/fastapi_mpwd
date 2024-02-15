""" Tag model. """
from datetime import datetime

from pydantic import BaseModel


class TagIn(BaseModel):
    """Tag input model."""

    tag: str


class Tag(BaseModel):
    """Tag model."""

    tag: str
    created: datetime
    secret: str


class TagOut(BaseModel):
    """Tag output model."""

    tag: str
    created: datetime
