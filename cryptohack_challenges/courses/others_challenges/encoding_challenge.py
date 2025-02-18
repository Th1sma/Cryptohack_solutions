from pwn import *  # pip install pwntools
import json
import base64
import codecs
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Connexion au serveur
r = remote('socket.cryptohack.org', 13377, level='debug')

# Fonction pour recevoir des données JSON
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

# Fonction pour envoyer des données JSON
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

# Fonction pour décoder les données reçues
def decoding_data_received(received):
    if received["type"] == "base64":
        decoded = base64.b64decode(received["encoded"]).decode()
    elif received["type"] == "hex":
        decoded = bytes.fromhex(received["encoded"]).decode()
    elif received["type"] == "rot13":
        decoded = codecs.decode(received["encoded"], 'rot_13')
    elif received["type"] == "bigint":
        decoded = long_to_bytes(int(received["encoded"], 16)).decode()
    elif received["type"] == "utf-8":
        decoded = ''.join([chr(c) for c in received["encoded"]])
    else:
        print("Type not detected")
    return decoded

# Boucle principale
a = 0
while a < 100:
    # Recevoir les données du serveur
    received = json_recv()

    print("===== Received informations =====")
    print("Received type: ", received["type"])
    print("Received encoded value: ", received["encoded"])
    print("=================================")

    # Ce que j'envoie comme requête au serveur
    to_send = {
        "decoded": "test"
    }

    # Envoyer la réponse au serveur
    json_send(to_send)
    
    # Réponse après envoie
    if "error" in response:
        print("Decoding failed")
        a += 1
    elif "flag" in response:
        print("Flag found: ", response["flag"])
        break
