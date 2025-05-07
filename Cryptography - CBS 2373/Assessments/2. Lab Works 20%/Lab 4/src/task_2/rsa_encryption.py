from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_encrypt_decrypt_user_input():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    plaintext = input("Enter a short message to encrypt using RSA: ").encode()

    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(plaintext)

    decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted = decipher.decrypt(ciphertext)

    print(f"\nEncrypted (hex): {ciphertext.hex()}")
    print(f"Decrypted: {decrypted.decode()}")

rsa_encrypt_decrypt_user_input()
