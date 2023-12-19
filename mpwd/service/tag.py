from datetime import datetime

from tinydb import TinyDB, where

from mpwd.model.tag import Tag, TagOut

db = TinyDB("db.json", indent=4, separators=(",", ": "))


def create(tag: Tag) -> Tag:
    tag_date = tag.created
    if tag_date and isinstance(tag_date, datetime):
        tag.created = tag_date.strftime("%Y-%m-%d %H:%M:%S")
    db.insert(tag.model_dump())
    return {"tag": "created"}


def get(tag_str: str) -> TagOut:
    tag = db.search(where("tag") == tag_str)
    if tag:
        return TagOut(**tag[0])
    else:
        return TagOut(tag="not found", created=datetime.now())
