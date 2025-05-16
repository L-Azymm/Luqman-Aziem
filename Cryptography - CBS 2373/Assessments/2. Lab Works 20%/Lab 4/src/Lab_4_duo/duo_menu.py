import os
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib

# Output folder setup
OUTPUT_DIR = "output_files"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ------------------ AES ------------------
def aes_encrypt():
    message = input("Enter message to encrypt (AES): ").encode()
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(message)

    enc_file = input("Enter file name for encrypted message (e.g. msg.enc): ")
    key_file = input("Enter file name for AES key (e.g. key.key): ")

    with open(os.path.join(OUTPUT_DIR, enc_file), "wb") as f:
        f.write(cipher.nonce + tag + ciphertext)
    with open(os.path.join(OUTPUT_DIR, key_file), "wb") as f:
        f.write(key)

    print("✅ AES encryption done. Files saved to output_files/")

def aes_decrypt():
    enc_file = input("Enter encrypted file name: ")
    key_file = input("Enter AES key file name: ")

    with open(os.path.join(OUTPUT_DIR, enc_file), "rb") as f:
        data = f.read()
    nonce, tag, ciphertext = data[:16], data[16:32], data[32:]

    with open(os.path.join(OUTPUT_DIR, key_file), "rb") as f:
        key = f.read()

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        decrypted = cipher.decrypt_and_verify(ciphertext, tag)
        print("✅ AES decryption successful:\n", decrypted.decode())
    except ValueError:
        print("❌ AES decryption failed.")

# ------------------ RSA ------------------
def rsa_encrypt():
    message = input("Enter message to encrypt (RSA): ").encode()
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(message)

    enc_file = input("Enter file name for encrypted message (e.g. msg.enc): ")
    pub_file = input("Enter public key file name (e.g. pub.pem): ")
    priv_file = input("Enter private key file name (e.g. priv.pem): ")

    with open(os.path.join(OUTPUT_DIR, enc_file), "wb") as f:
        f.write(ciphertext)
    with open(os.path.join(OUTPUT_DIR, pub_file), "wb") as f:
        f.write(public_key)
    with open(os.path.join(OUTPUT_DIR, priv_file), "wb") as f:
        f.write(private_key)

    print("✅ RSA encryption done. Files saved.")

def rsa_decrypt():
    enc_file = input("Enter encrypted file name: ")
    priv_file = input("Enter private key file name: ")

    with open(os.path.join(OUTPUT_DIR, enc_file), "rb") as f:
        ciphertext = f.read()
    with open(os.path.join(OUTPUT_DIR, priv_file), "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)
    try:
        decrypted = cipher.decrypt(ciphertext)
        print("✅ RSA decryption successful:\n", decrypted.decode())
    except ValueError:
        print("❌ RSA decryption failed.")

# ------------------ SHA-256 ------------------
def sha256_hashing():
    msg1 = input("Enter first message to hash: ").encode()
    msg2 = input("Enter second message to hash: ").encode()

    hash1 = hashlib.sha256(msg1).hexdigest()
    hash2 = hashlib.sha256(msg2).hexdigest()

    print(f"\nHash 1: {hash1}")
    print(f"Hash 2: {hash2}")

    if hash1 == hash2:
        print("✅ Hashes match")
    else:
        print("❌ Hashes are different")

# ------------------ Digital Signature ------------------
def sign_message():
    message = input("Enter message to sign: ").encode()
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    hash_obj = SHA256.new(message)
    signature = pkcs1_15.new(RSA.import_key(private_key)).sign(hash_obj)

    sig_file = input("Enter signature file name (e.g. sig.bin): ")
    pub_file = input("Enter public key file name (e.g. pub.pem): ")
    msg_file = input("Enter file name to save the message (e.g. msg.txt): ")

    with open(os.path.join(OUTPUT_DIR, sig_file), "wb") as f:
        f.write(signature)
    with open(os.path.join(OUTPUT_DIR, pub_file), "wb") as f:
        f.write(public_key)
    with open(os.path.join(OUTPUT_DIR, msg_file), "wb") as f:
        f.write(message)

    print("✅ Message signed and files saved.")

def verify_signature():
    sig_file = input("Enter signature file name: ")
    pub_file = input("Enter public key file name: ")
    msg_file = input("Enter message file name: ")

    with open(os.path.join(OUTPUT_DIR, sig_file), "rb") as f:
        signature = f.read()
    with open(os.path.join(OUTPUT_DIR, pub_file), "rb") as f:
        public_key = RSA.import_key(f.read())
    with open(os.path.join(OUTPUT_DIR, msg_file), "rb") as f:
        message = f.read()

    hash_obj = SHA256.new(message)
    try:
        pkcs1_15.new(public_key).verify(hash_obj, signature)
        print("✅ Signature is valid.")
    except (ValueError, TypeError):
        print("❌ Signature is invalid or message has been tampered.")

# ------------------ Menu ------------------
def menu():
    while True:
        print("_______________________")
        print("\n| --> CRYPTO MENU <-- |")
        print("_______________________")
        print("\n  1. AES")
        print("  2. RSA")
        print("  3. SHA-256 Hashing")
        print("  4. Digital Signature")
        print("  0. Exit")
        choice = input("\n Select option: ")

        if choice == "1":
            while True:
                print("\nAES Options:")
                print("1. Encrypt")
                print("2. Decrypt")
                print("0. Back")
                sub = input("Select: ")
                if sub == "1":
                    aes_encrypt()
                elif sub == "2":
                    aes_decrypt()
                elif sub == "0":
                    break
                else:
                    print("❌ Invalid choice.")
        elif choice == "2":
            while True:
                print("\nRSA Options:")
                print("1. Encrypt")
                print("2. Decrypt")
                print("0. Back")
                sub = input("Select: ")
                if sub == "1":
                    rsa_encrypt()
                elif sub == "2":
                    rsa_decrypt()
                elif sub == "0":
                    break
                else:
                    print("❌ Invalid choice.")
        elif choice == "3":
            sha256_hashing()
        elif choice == "4":
            while True:
                print("\nDigital Signature Options:")
                print("1. Sign Message")
                print("2. Verify Signature")
                print("0. Back")
                sub = input("Select: ")
                if sub == "1":
                    sign_message()
                elif sub == "2":
                    verify_signature()
                elif sub == "0":
                    break
                else:
                    print("❌ Invalid choice.")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option.")

menu()
