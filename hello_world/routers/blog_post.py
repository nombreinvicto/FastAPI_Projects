from fastapi import APIRouter, status, Response
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/blog",
                   tags=["blog"])


# %% ##################################################################
# create all the pydantic models
class BlogModel(BaseModel):
    title: str
    content: str
    published: Optional[bool]


# %% ##################################################################
@router.post("/new")
def create_blog(blog: BlogModel):
    return f"got blog with title: {blog.title} and content: {blog.content}"


@router.post("/new/{id}")
def create_blog(blog: BlogModel, id: int, version: int = 1):
    return {
        'id': id,
        'data': blog,
        'version': version
    }
