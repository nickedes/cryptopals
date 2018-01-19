# http://cryptopals.com/sets/1/challenges/1
import base64 as b

# given Hex!
string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# expected
result = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t".encode()

# Decodes from hex to bytes object
encoded = bytes.fromhex(string)

# Encode the bytes object using Base64
b64encode = b.b64encode(encoded)

if b64encode == result:
    print("done!")
else:
    print("Incomplete!")
