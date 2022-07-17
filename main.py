import os
import sys
import base64
from PIL import Image
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.Memo import Base
from models.Memo import Memo


def show_module_choices():
    print("Choose a module: ")
    print("1. list all memo items")
    print("2. add or update items")
    print("3. open memo")
    choice = input()
    return choice


def check_for_file_existence():
    filename = input("Enter file name: ")
    filepath = os.path.join(os.getcwd(), "input", filename)
    if not os.path.exists(filepath):
        print(f"file: {filepath} does not exists!")
        sys.exit(1)

    return filepath


def query_all_items(db_session):
    return db_session.query(Memo).all()


def query_items_by_name(db_session, memo_name):
    result = db_session.query(Memo).filter_by(NAME=memo_name).all()
    return result


def add_or_update(db_session):
    filepath = check_for_file_existence()
    memo_name = input("input memo item name: ")
    with open(filepath, "rb") as file_input:
        content = file_input.read()
        encoded = base64.b64encode(content).decode()

    check_item_exists = query_items_by_name(db_session, memo_name)
    if len(check_item_exists) > 0:
        print(f"item already exists, updating..., name: {memo_name}")
        original = check_item_exists[0]
        original.CONTENT = encoded
    else:
        memo = Memo(NAME=memo_name, CONTENT=encoded)
        print(f"adding item..., name: {memo_name}")
        db_session.add(memo)

    db_session.commit()
    print(f"Done")


def open_memo(db_session, item_name):
    image_path = os.path.join(os.getcwd(), "output", item_name) + ".jpg"
    if not os.path.exists(image_path):
        # look for item in database
        print("image not found in output folder, fetching from database...")
        memo_item_arr = query_items_by_name(db_session, item_name)
        if not memo_item_arr:
            print("item not in database, please add content first!")
            return
        print(memo_item_arr)
        memo_item = memo_item_arr[0]

        with open(image_path, "wb") as output:
            output.write(base64.b64decode(memo_item.CONTENT))
        print("saving a copy to output folder...")

    print("opening image...")
    image = Image.open(image_path)
    image.show()


def execute_module(db_session, choice):
    print()
    if choice == "1":
        res = query_all_items(db_session)
        if len(res) == 0:
            print("no data yet!")
        else:
            for elem in res:
                print(f"{elem.ID}. {elem.NAME}")
            print()
    elif choice == "2":
        add_or_update(db_session)
    elif choice == "3":
        item_name = input("Input memo item name: ")
        open_memo(db_session, item_name)


def main():
    # check for database
    if not os.path.exists(os.path.join(os.getcwd(), "memo_db")):
        print("Database not found! please provide database!")
        sys.exit(1)

    engine = create_engine("sqlite:///memo_db", echo=False)
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        choice = show_module_choices()
        # will create table if doesn't exists
        Base.metadata.create_all(engine)
        execute_module(session, choice)


if __name__ == "__main__":
    main()
