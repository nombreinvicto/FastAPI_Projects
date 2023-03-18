from fastapi import APIRouter, status, Response, Query, Body, Path
from pydantic import BaseModel
from typing import Optional, List

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
                   id: int = Path(),
                   comment_id: int = Query(None,
                                           title='id of the comment',
                                           description='some description',
                                           alias='commentId',
                                           deprecated=True),
                   content: str = Body(min_length=10),
                   v: List[str] = Query(None)):
    return {
        'blog': blog,
        'id': id,
        'comment_id': comment_id,
        'content': content,
        'version': v
    }
