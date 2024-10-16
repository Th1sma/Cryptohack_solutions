string_hex = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

string_bytes = bytes.fromhex(string_hex)

for key in range(256):

    decrypted = bytes([b ^ key for b in string_bytes])

    try:
        print(f"Key: {key}, Decrypted: {decrypted.decode('utf-8')}")

    except UnicodeDecodeError:
        continue
