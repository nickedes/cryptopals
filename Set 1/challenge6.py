import base64 as b
from challenge3 import getScore


def single_char_xor(lines):
    best_score = -1000
    dec_str = lines
    for i in range(256):
        plain = ''
        for x in dec_str:
            plain += chr(ord(x) ^ i)
        score = getScore(plain)
        if score > best_score:
            best_score = score
            key = i
    return key


def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result


def hamming2(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def full_ham_dist(data, keysize):
    total_hamdist = 0
    for i in range(len(data)//keysize):
        total_hamdist += hamming2(tobits(data[i*keysize: (i+1)*keysize]),
                                  tobits(data[(i+1)*keysize: (i+2)*keysize]))
    total_hamdist /= keysize
    return total_hamdist


if __name__ == "__main__":

    with open('challenge-data-6.txt', 'r') as f:
        data = f.read()

    b64decode = b.b64decode(data)
    # print(b64decode)
    text = ""
    for x in b64decode:
        text += chr(x)

    max_hamdist = 100000
    for keysize in range(2, 40):
        ham_dist = full_ham_dist(text, keysize)
        if ham_dist < max_hamdist:
            max_hamdist = ham_dist
            keylen = keysize

    # print(max_hamdist, keylen)
    # Now that you probably know the KEYSIZE: break the ciphertext into blocks
    # of KEYSIZE length.Now transpose the blocks: make a block that is the
    # first byte of every block, and a block that is the second byte of every
    # block, and so on.
    blocks = [text[i::keylen] for i in range(keylen)]
    key = ""
    for block in blocks:
        key += chr(single_char_xor(block))
    print(key)

    plain = ''
    for i in range(len(text)):
        plain += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    print(plain)
