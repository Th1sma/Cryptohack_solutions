key_1_hex = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key_2_key_1_hex = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
key_3_key_2_hex = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_key_1_2_3_hex = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


def decoding(key_a, key_b):

    return bytes(x ^ y for x, y in zip(key_a, key_b))


key_1 = bytes.fromhex(key_1_hex)
key_2_key_1_xor = bytes.fromhex(key_2_key_1_hex)
key_3_key_2_xor = bytes.fromhex(key_3_key_2_hex)
flag_key_1_2_3_xor = bytes.fromhex(flag_key_1_2_3_hex)

key_2 = decoding(key_2_key_1_xor, key_1)
key_3 = decoding(key_3_key_2_xor, key_2)

flag = decoding(flag_key_1_2_3_xor, decoding(decoding(key_1, key_2), key_3))
print("The flag is:")
print(flag)
