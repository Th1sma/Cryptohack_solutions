from cryptography import x509

filename = "2048b-rsa-example-cert_3220bd92e30015fe4fbeb84a755e7ca5.der"

try:
    # Charger le certificat
    with open(filename, "rb") as f:
        cert = x509.load_der_x509_certificate(f.read())

    # Extraction du modulus
    modulus = cert.public_key().public_numbers().n
    print("Modulus:", modulus)

except Exception as e:
    print("Erreur :", e)
