from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

import hashlib

# === AES ===
def aes_encrypt_decrypt():
    print("\n=== AES Encryption/Decryption ===")
    key = get_random_bytes(32)
    cipher = AES.new(key, AES.MODE_CBC)
    text = input("Enter message to encrypt (AES): ").encode()
    ct = cipher.encrypt(pad(text, AES.block_size))
    iv = cipher.iv
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    pt = unpad(cipher_dec.decrypt(ct), AES.block_size)
    print(f"Ciphertext: {ct.hex()}")
    print(f"Decrypted: {pt.decode()}")

# === RSA ===
def rsa_encrypt_decrypt():
    print("\n=== RSA Encryption/Decryption ===")
    key = RSA.generate(2048)
    pubkey = key.publickey().export_key()
    privkey = key.export_key()
    text = input("Enter message to encrypt (RSA): ").encode()
    cipher = PKCS1_OAEP.new(RSA.import_key(pubkey))
    ct = cipher.encrypt(text)
    decipher = PKCS1_OAEP.new(RSA.import_key(privkey))
    pt = decipher.decrypt(ct)
    print(f"Ciphertext: {ct.hex()}")
    print(f"Decrypted: {pt.decode()}")

# === Hashing ===
def hash_sha256():
    print("\n=== SHA-256 Hashing ===")
    msg = input("Enter message to hash: ").encode()
    h = hashlib.sha256(msg).hexdigest()
    print(f"Hash: {h}")

# === Digital Signature ===
def digital_signature_user_input():
    print("\n=== Digital Signature ===")
    key = RSA.generate(2048)
    pubkey = key.publickey().export_key()
    message = input("Enter a message to digitally sign: ").encode()
    hash_obj = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash_obj)
    print(f"Signature: {signature.hex()}")
    
    tampered = input("Enter message again to verify: ").encode()
    hash_verify = SHA256.new(tampered)
    try:
        pkcs1_15.new(RSA.import_key(pubkey)).verify(hash_verify, signature)
        print("✅ Signature is valid.")
    except (ValueError, TypeError):
        print("❌ Signature is invalid.")

# === Menu ===
def menu():
    while True:
        print("\n===== Cryptography Lab Menu =====")
        print("1. AES Encryption/Decryption")
        print("2. RSA Encryption/Decryption")
        print("3. Hashing (SHA-256)")
        print("4. Digital Signature")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == '1':
            aes_encrypt_decrypt()
        elif choice == '2':
            rsa_encrypt_decrypt()
        elif choice == '3':
            hash_sha256()
        elif choice == '4':
            digital_signature_user_input()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()
