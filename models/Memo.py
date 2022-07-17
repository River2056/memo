from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class Memo(Base):
    __tablename__ = "MEMO_LIST"

    ID = Column(Integer, Sequence("ID"), primary_key=True)
    NAME = Column(String)
    CONTENT = Column(String)

    def __repr__(self):
        return f"Memo[id: {self.ID}, name: {self.NAME}, content: {self.CONTENT[0:25]}]"
