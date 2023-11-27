import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import sys

#GEN priv and pub keys
def genLaptopKeys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    # Save Private Key to File
    print("Writing Private and Public key files\n")
    with open("laptop_priv_key.pem", "wb") as key_file:
        key_file.write(private_pem)

    # Save Pub Key to File
    with open("laptop_pub_key.pem", "wb") as key_file:
        key_file.write(public_pem)

genLaptopKeys()