from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/greet/{name}")
def greet(name: str, q: Union[str, None] = None):
    return {"name": name, "q": q}
