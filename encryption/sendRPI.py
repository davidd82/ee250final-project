from cryptography.fernet import Fernet

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import utils
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

import sys

# RPI encrypts message with sym key and uses priv key to make the hash and saves it

def send(availability):
    with open("encryption/rpi_priv_key.pem", "rb") as key_file:
        # Use the appropriate function "load_pem_private_key" or
        # "load_pem_public_key"
        rpi_priv_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
        )

    with open("encryption/laptop_pub_key.pem", "rb") as key_file:
        # Use the appropriate function "load_pem_private_key" or
        # "load_pem_public_key"
        laptop_pub_key = serialization.load_pem_public_key(
            key_file.read(),
            backend=default_backend()
        )

    if(availability == 0):
            #with open("message.txt", "r") as msg_file:
            # asc_msg = msg_file.read()
        message = bytes("0", 'utf-8')
    else: 
        message = bytes("1", 'utf-8')

    # symmetrical key

    with open("encryption/symkey.key", "rb") as key_file:
        symkey = key_file.read()

    cipher_suite = Fernet(symkey)
    encrypted_msg = cipher_suite.encrypt(message)

    h = hashes.SHA256()
    hasher = hashes.Hash(h)
    hasher.update(encrypted_msg)
    # hashes the sym encrypted message for digest
    digest = hasher.finalize()

    encrypted_hash = rpi_priv_key.sign(  # THIS IS TO GET THE SIGNATURE
        digest,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        utils.Prehashed(h)
    )

    # digitally signed data
    signed_enc_msg = encrypted_hash + encrypted_msg

    with open("rpi_signed_msg.bin", "wb") as bin_file:
        bin_file.write(signed_enc_msg)

send(1)