from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import hashlib


def aes_encrypt_decrypt():
    print("\n=== AES Symmetric Encryption ===")
    key = get_random_bytes(32)  # 256-bit key
    cipher = AES.new(key, AES.MODE_CBC)

    message = input("Enter a message to encrypt with AES: ").encode()
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    iv = cipher.iv

    decipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

    print(f"\nEncrypted (hex): {ciphertext.hex()}")
    print(f"Decrypted: {decrypted.decode()}")


def rsa_encrypt_decrypt():
    print("\n=== RSA Asymmetric Encryption ===")
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    message = input("Enter a message to encrypt with RSA: ").encode()
    cipher = PKCS1_OAEP.new(RSA.import_key(public_key))
    ciphertext = cipher.encrypt(message)

    decipher = PKCS1_OAEP.new(RSA.import_key(private_key))
    decrypted = decipher.decrypt(ciphertext)

    print(f"\nEncrypted (hex): {ciphertext.hex()}")
    print(f"Decrypted: {decrypted.decode()}")


def hash_sha256():
    print("\n=== SHA-256 Hashing & Comparison ===")

    def compute_sha256(data):
        sha = hashlib.sha256()
        sha.update(data)
        return sha.hexdigest()

    msg1 = input("Enter first message to hash: ").encode()
    msg2 = input("Enter second message to hash: ").encode()

    hash1 = compute_sha256(msg1)
    hash2 = compute_sha256(msg2)

    print(f"\nHash 1: {hash1}")
    print(f"Hash 2: {hash2}")

    if hash1 == hash2:
        print("✅ Hashes are the same (messages are identical)")
    else:
        print("❌ Hashes are different (messages are not the same)")


def digital_signature():
    print("\n=== Digital Signature with RSA ===")
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    message = input("Enter a message to digitally sign: ").encode()

    # Step 1: Hash the message
    hash_obj = SHA256.new(message)

    # Step 2: Sign the hash with private key
    signature = pkcs1_15.new(key).sign(hash_obj)
    print(f"\nDigital Signature (hex): {signature.hex()}")

    # Step 3: Tamper test (optional)
    tamper = input("Do you want to tamper with the message before verification? (yes/no): ").lower()
    if tamper == "yes":
        message = b"tampered message"
        print("⚠️ Message has been tampered.")

    # Step 4: Verify signature with public key
    try:
        verifier = pkcs1_15.new(RSA.import_key(public_key))
        verifier.verify(SHA256.new(message), signature)
        print("✅ Signature is valid. The message has not been changed.")
    except (ValueError, TypeError):
        print("❌ Signature is invalid. The message may have been tampered.")


# ====== Menu Loop ======
while True:
    print("\n=== Cryptography Lab Menu ===")
    print("1. AES (Symmetric Encryption)")
    print("2. RSA (Asymmetric Encryption)")
    print("3. Hashing (SHA-256)")
    print("4. Digital Signature")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        aes_encrypt_decrypt()
    elif choice == "2":
        rsa_encrypt_decrypt()
    elif choice == "3":
        hash_sha256()
    elif choice == "4":
        digital_signature()
    elif choice == "5":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please select 1-5.")
