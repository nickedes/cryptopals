import base64 as b
# Using this! https://github.com/dlitz/pycrypto
from Crypto.Cipher import AES

if __name__ == '__main__':
    with open('challenge-data-7.txt', 'r') as f:
        data = f.read()

    ciphertext = b.b64decode(data)
    key = 'YELLOW SUBMARINE'

    # Default mode for AES in package is ECB
    cipher = AES.new(key)

    encodedText = cipher.decrypt(ciphertext)
    # plaintext = encodedText.decode()
    # Decode the bytes to String!
    plaintext = str(encodedText, 'utf-8')
    print(plaintext)
