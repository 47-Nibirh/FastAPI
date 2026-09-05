# pyright: reportMissingImports=false
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "Hello Nibirhs World"

@app.get("/about")
def about():
    return "Hello from about page World"