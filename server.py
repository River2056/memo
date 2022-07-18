import os
import sys
from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Memo import Base
from models.Memo import Memo
from models.MemoItem import MemoItem

app = FastAPI()

# check for database
if not os.path.exists(os.path.join(os.getcwd(), "memo_db")):
    print("Database not found! please provide database!")
    sys.exit(1)

engine = create_engine("sqlite:///memo_db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)


@app.get("/")
def fetch_all_memo():
    memo_list = session.query(Memo).all()
    remap_list = list(map(lambda x: {"id": x.ID, "name": x.NAME}, memo_list))
    return remap_list


@app.get("/name/{memo_name}")
def fetch_memo_content_by_name(memo_name: str):
    memo = session.query(Memo).filter(Memo.NAME == memo_name).first()
    return memo


@app.post("/new/")
def add_new(memo: MemoItem):
    print("add new memo...")
    print(memo)
    return "done!"


@app.get("/greet/{name}")
def greet(name: str, q: Union[str, None] = None):
    return {"name": name, "q": q}
