import base64

hexa_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

bytes_decoding = bytes.fromhex(hexa_string)

print(base64.b64encode(bytes_decoding))
