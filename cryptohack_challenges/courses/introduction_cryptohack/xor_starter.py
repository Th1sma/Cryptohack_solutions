from Crypto.Util.number import bytes_to_long

string = "label"
integer = 13

# Convertir la chaîne en bytes
string_to_bytes = string.encode()

# Appliquer XOR sur chaque byte de la chaîne
xor_bytes = bytes([b ^ integer for b in string_to_bytes])

print("The flag is:")
print(xor_bytes)