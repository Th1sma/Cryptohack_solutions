from Crypto.Util.number import bytes_to_long

string = "label"
integer = 13

string_to_bytes = string.encode()

xor_bytes = bytes([b ^ integer for b in string_to_bytes])

print("The flag is:")
print(xor_bytes)
