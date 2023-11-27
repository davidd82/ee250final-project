from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
import sys

# Laptop verifies if the received digitally signed data is from RPI
with open("rpi_signed_msg.bin", "rb") as bin_file:
    raw_contents = bin_file.read()
    # Separate the hash and the remaining part of the message
    recv_encrypted_hash = raw_contents[:256]
    recv_encrypted_msg = raw_contents[256:]

with open("rpi_pub_key.pem", "rb") as key_file:
    # Use the appropriate function "load_pem_private_key" or
    # "load_pem_public_key"
    sign_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

h = hashes.SHA256()
hasher = hashes.Hash(h)
hasher.update(recv_encrypted_msg)  # fill me in.
digest = hasher.finalize()

# verifies place of origin from laptop
sign_key.verify(
    recv_encrypted_hash,
    digest,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    utils.Prehashed(h)
)

# opens symmetrical key
with open("symkey.key", "rb") as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)
decrypted_text = cipher_suite.decrypt(recv_encrypted_msg)

with open("out.txt", "w") as out_file:
    out_file.write(str(decrypted_text, 'utf-8'))