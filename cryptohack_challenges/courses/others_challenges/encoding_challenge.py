from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes
import sys

r = remote("socket.cryptohack.org", 13377, level="debug")


def json_recv():
    line = r.recvline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def decode(enc_type, encoded_data):
    if enc_type == "base64":
        return base64.b64decode(encoded_data).decode()
    elif enc_type == "hex":
        return bytes.fromhex(encoded_data).decode()
    elif enc_type == "rot13":
        return codecs.decode(encoded_data, "rot_13")
    elif enc_type == "bigint":
        return long_to_bytes(int(encoded_data, 16)).decode()
    elif enc_type == "utf-8":
        return "".join([chr(c) for c in encoded_data])
    else:
        print(f"[!] Unknown encoding type: {enc_type}")
        return None


while True:

    received = json_recv()

    if "flag" in received:
        print("FLAG: %s" % received["flag"])
        sys.exit(0)

    decoded_value = decode(received["type"], received["encoded"])

    if decoded_value is None:
        print("[!] Failed to decode the data, exiting.")
        sys.exit(1)

    print("===== Received informations =====")
    print("Received type: ", received["type"])
    print("Received encoded value: ", received["encoded"])
    print("Decoded value: ", decoded_value)
    print("=================================")

    to_send = {"decoded": decoded_value}

    json_send(to_send)
