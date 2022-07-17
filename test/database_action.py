import os
import base64
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Memo import Memo

def add_new_item(db_session, item_name, item_content):
    filename = input("Enter file name: ")
    os.path.exists(filename)
    memo = Memo(name=item_name, content=item_content)
    print(memo)


def main():
    engine = create_engine("sqlite:///memo_db", echo=True)
    session = sessionmaker(bind=engine)

    with open("./subnet.png", "rb") as file_input:
        content = file_input.read()
        encoded = base64.b64encode(content).decode()

    

if __name__ == "__main__":
    main()
