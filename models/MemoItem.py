from pydantic import BaseModel


class MemoItem(BaseModel):
    name: str
    content: str
