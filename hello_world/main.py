from fastapi import FastAPI
from hello_world.routers import blog_get
from hello_world.routers import blog_post

# %% ##################################################################
# server python_file:fastapi_object --reload
# e.g uvicorn main:app --reload
# Pycharm -> C:\Users\mhasa\GitHub\venvs\fastapi\Scripts\python.exe -m uvicorn hello_world.main:app --reload --reload-delay 10
app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


# %% ##################################################################

@app.get("/")
def index():
    return {"message": 'Hello World'}
