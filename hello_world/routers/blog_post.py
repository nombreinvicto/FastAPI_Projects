from fastapi import APIRouter, status, Response, Query
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


@router.post("/new/{id}/comment")
def create_comment(blog: BlogModel,
                   id: int,
                   comment_id: int = Query(title='id of the comment',
                                           description='some description')):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id
    }
