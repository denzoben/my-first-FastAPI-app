from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def home():
    return({"message": "Welcome to home page of fast api!"})