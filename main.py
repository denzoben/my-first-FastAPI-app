from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from random import randrange

from validator import Post

app = FastAPI()

my_posts = [
            {"tittle": "My first content title", "content": "My first content", "id": 1},
            {"tittle": "My second content title", "content": "My second content", "id": 2}
        ]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_post_index(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i

@app.get("/")
def home():
    return({"message": "Welcome to the home page of Fast API!"})

@app.get("/posts")
def show_posts():
    return({"message": my_posts})

@app.get("/posts/{id}")
def show_specific_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id:{id} not found!")
    return({"message": post})

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    new_post = post.model_dump()    # use to convert the payload to dictionary/JSON.
    new_post["id"] = randrange(1, 9999999)
    my_posts.append(new_post)
    return({"message": new_post})

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_post_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id:{id} not found!")
    my_posts.pop(index)
    return({"message": "Post deleted successfully!"})

@app.put("/posts/{id}")
def update_post(id:int, post: Post):
    index = find_post_index(id)
    if not index:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"Post with id:{id} not found!")
    
    updated_post = post.model_dump()
    print(updated_post)
    updated_post["id"] = id
    my_posts[index] = updated_post
    return({"message": "Post updated successfully!"})

