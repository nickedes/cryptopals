from challenge3 import getScore
import time

with open('challenge-data-4.txt', 'r') as f:
    data = f.read()

lines = data.split('\n')

strings = []
for line in lines:
    dec_str = bytes.fromhex(line)
    for i in range(256):
        plain = ''
        for x in dec_str:
            plain += chr(x ^ i)
        score = getScore(plain)
        strings.append((plain, score))

sorted_byscore = sorted(strings, key=lambda x: x[1], reverse=True)

# print(sorted_byscore[:5])
for x in sorted_byscore[:5]:
    print(x[0], "Score : ", x[1])
