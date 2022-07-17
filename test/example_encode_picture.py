import base64


def main():
    with open("./subnet.png", "rb") as file:
        content = file.read()
        encoded = base64.b64encode(content).decode()

    # print(encoded[0:10])

    with open("./test.txt", "wt", encoding="utf-8") as output:
        output.write(encoded)


if __name__ == "__main__":
    main()
