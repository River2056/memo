import base64
from PIL import Image


def main():
    with open("./test.txt", "rt", encoding="utf-8") as file_input:
        content = file_input.read()
        bytes_info = base64.b64decode(content)

    with open("./text.jpg", "wb") as output:
        output.write(bytes_info)

    image = Image.open("./text.jpg")
    image.show()


if __name__ == "__main__":
    main()
