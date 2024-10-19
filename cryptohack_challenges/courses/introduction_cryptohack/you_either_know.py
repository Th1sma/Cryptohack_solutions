from Crypto.Util.number import *

string = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
integer = 12

string_to_bytes = bytes.fromhex(string)

xor_bytes = xor(string_to_bytes, key)
xor_bytes = xor(string_to_bytes, "myXORkey")

print("The flag is:")
print(xor_bytes)
