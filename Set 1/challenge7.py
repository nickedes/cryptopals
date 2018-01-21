import base64 as b


if __name__ == '__main__':
    with open('challenge-data-7.txt', 'r') as f:
        data = f.read()
    b64decode = b.b64decode(data)
    print(b64decode)
