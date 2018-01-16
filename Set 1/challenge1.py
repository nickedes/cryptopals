# http://cryptopals.com/sets/1/challenges/1
import base64 as b

# given Hex!
string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# Decodes from hex to bytes object
encoded = bytes.fromhex(string)

# Encode the bytes object using Base64
b64encode = b.b64encode(encoded)

print(b64encode)
