"""
DES Encryption and Decryption Demo

A simple implementation of the Data Encryption Standard (DES)
using the PyCryptodome library.

"""

from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad


def des_encrypt_decrypt():
    print("=" * 40)
    print("     DES Encryption & Decryption")
    print("=" * 40)

    key = b'8bytekey'  # DES requires an 8-byte key

    cipher = DES.new(key, DES.MODE_ECB)

    plaintext = input("\nEnter plaintext: ").encode()

    # Encrypt
    ciphertext = cipher.encrypt(pad(plaintext, 8))
    print("\nEncrypted Ciphertext:")
    print(ciphertext)

    # Decrypt
    decrypted = unpad(cipher.decrypt(ciphertext), 8)

    print("\nDecrypted Plaintext:")
    print(decrypted.decode())


if __name__ == "__main__":
    des_encrypt_decrypt()
