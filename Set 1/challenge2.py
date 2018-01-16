# http://cryptopals.com/sets/1/challenges/2
string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"

required = "746865206b696420646f6e277420706c6179"

# perform Hex decoding!
dec_str1 = bytes.fromhex(string1)
dec_str2 = bytes.fromhex(string2)

# print(dec_str1, dec_str2)

xor_string = ''

# Xor
for x in range(len(dec_str1)):
    # print(dec_str1[x], dec_str2[x])
    xor_string += chr(dec_str1[x] ^ dec_str2[x])

# Encoding string
encoded_xor_string = xor_string.encode('ascii')

hex_encode = encoded_xor_string.hex()

if hex_encode == required:
    print("DONE!")
