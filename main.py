from fastapi import FastAPI
from fastapi.params import Body

from validator import Post

app = FastAPI()

@app.get("/")
def home():
    return({"message": "Welcome to the home page of Fast API!"})

@app.get("/posts")
def show_posts():
    return({"message": "Show all posts"})

@app.post("/posts")
def create_post(post: Post):
    print(post.rating)
    print(post.model_dump()) # use to convert the payload to dictionary/JSON.
    return({"message": "new post"})