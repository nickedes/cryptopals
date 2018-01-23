import base64 as b
from challenge3 import getScore
from itertools import combinations


def hamming_distance(s1, s2):
    """Calculate the Hamming distance between two bit strings"""
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def repeating_key_xor(plaintext, key):
    """Implements the repeating-key XOR encryption."""
    ciphertext = ''
    i = 0

    for byte in plaintext:
        ciphertext += chr(byte ^ key[i])

        i = (i + 1) % len(key)
    return ciphertext


def singlechar_xor(block):
    possiblekeys = []
    for keysize in range(256):
        plain = b''
        text = ''
        for x in block:
            plain += bytes(x ^ keysize)
            text += chr(x ^ keysize)
        score = getScore(text)
        result = {
            'key': keysize,
            'score': score,
            'plaintext': plain
        }
        possiblekeys.append(result)

    # Return the candidate with the highest English score
    # print(sorted(possiblekeys, key=lambda x: x['score'], reverse=True)[0])
    return sorted(possiblekeys, key=lambda x: x['score'], reverse=True)[0]


def break_repeating_xor(data):
    """
    input : b64 decoded data
    Breaks the repeating key XOR
    """
    # save all the normalized distances
    dists = {}

    for keylen in range(2, 40):
        chunks = [data[i:i + keylen] for i in range(0, len(data), keylen)][:4]
        # Sum the hamming distances between each pair of chunks
        distance = 0
        pairs = combinations(chunks, 2)
        for (x, y) in pairs:
            distance += hamming_distance(x, y)
        distance /= 6
        dists[keylen] = distance/keylen

    possible_key_sizes = sorted(dists, key=dists.get)[:3]
    possible_plaintexts = []
    for d in possible_key_sizes:
        key = b''

        # Break the ciphertext into blocks of key_size length
        for i in range(d):
            block = b''

            # Transpose the blocks: make a block that is the i-th byte of every
            # block
            for j in range(i, len(data), d):
                block += bytes([data[j]])

            # Solve each block as if it was single-character XOR
            key += bytes([singlechar_xor(block)['key']])

        # Store the candidate plaintext that we would get with the key that we
        # just found
        possible_plaintexts.append((repeating_key_xor(data, key), key))
    return max(possible_plaintexts, key=lambda k: getScore(k[0]))

if __name__ == "__main__":

    with open('challenge-data-6.txt', 'r') as f:
        data = f.read()

    b64decode = b.b64decode(data)
    result = break_repeating_xor(b64decode)
    print("Text :", result[0], "Key :", bytes.decode(result[1]))
