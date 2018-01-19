from challenge3 import getScore


def single_char_xor(lines):
    strings = []
    for line in lines:
        dec_str = bytes.fromhex(line)
        for key in range(256):
            plain = ''
            for x in dec_str:
                plain += chr(x ^ key)
            score = getScore(plain)
            strings.append((plain, score, key))

    result = sorted(strings, key=lambda x: x[1], reverse=True)[0]
    return result


if __name__ == '__main__':
    with open('challenge-data-4.txt', 'r') as f:
        data = f.read()

    lines = data.split('\n')
    result = single_char_xor(lines)
    print("Text :", result[0], "\nKey :", chr(result[2]))
