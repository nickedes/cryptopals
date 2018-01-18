# http://cryptopals.com/sets/1/challenges/3

freqtable = {"E": "12.02",
             "T": "9.10",
             "A": "8.12",
             "O": "7.68",
             "I": "7.31",
             "N": "6.95",
             "S": "6.28",
             "R": "6.02",
             "H": "5.92",
             "D": "4.32",
             "L": "3.98",
             "U": "2.88",
             "C": "2.71",
             "M": "2.61",
             "F": "2.30",
             "Y": "2.11",
             "W": "2.09",
             "G": "2.03",
             "P": "1.82",
             "B": "1.49",
             "V": "1.11",
             "K": "0.69",
             "X": "0.17",
             "Q": "0.11",
             "J": "0.10",
             "Z": "0.07"
             }


def getScore(plain):
    score = 0
    for char in plain:
        if not char.isalpha():
            # penalty
            score -= 5
        elif char.isalpha() and char.upper() in freqtable:
            score += float(freqtable[char.upper()])
    return score

if __name__ == '__main__':
    # hex encoded string
    hexencoded = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

    dec_str = bytes.fromhex(hexencoded)

    strings = []
    for i in range(256):
        plain = ''
        for x in dec_str:
            plain += chr(x ^ i)
        score = getScore(plain)
        strings.append((plain, score))

    # cOOKINGmcSLIKEAPOUNDOFBACON
    sorted_byscore = sorted(strings, key=lambda x: x[1], reverse=True)

    for x in sorted_byscore[:5]:
        print(x[0], "Score: ",x[1])
