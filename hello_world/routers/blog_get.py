from fastapi import APIRouter, status, Response
from enum import Enum

router = APIRouter(prefix="/blog",
                   tags=["blog"])


# %% ##################################################################
class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'


# %% ##################################################################
@router.get('/all')
def get_all_blogs(page, page_size):
    return {'message': f'All {page_size} blogs on page: {page}'}


@router.get("/type/{type}")
def get_blog_type(type: BlogType):
    return {'message': f'Blog Type: {type}'}


@router.get("/{id}")
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': f'Blog with id: {id} not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f"Blog with id: {id} found"}
