from cryptography.hazmat.primitives import serialization

file_path = "bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub"

try:
    # Charger et lire la clé publique
    with open(file_path, "rb") as f:
        key_data = f.read()

    # Extraire le modulus
    modulus = serialization.load_ssh_public_key(key_data).public_numbers().n
    print(f"Modulus (n): {modulus}")

except Exception as e:
    print(f"Erreur : {e}")
