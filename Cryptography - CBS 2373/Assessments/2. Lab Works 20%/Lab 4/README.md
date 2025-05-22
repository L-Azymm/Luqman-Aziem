# 🛡️ Lab 4 SOLO: Cryptographic Algorithms in Python

---

## 🎯 Objectives

This lab helps you understand and implement fundamental cryptographic techniques in Python:

- 🔐 AES Symmetric Encryption
- 🔑 RSA Asymmetric Encryption
- 🧮 SHA-256 Hashing
- ✍️ Digital Signatures using RSA

---

## 🧰 Requirements & Setup

### ✅ Tools

- Python 3.8+
- Terminal/Command Prompt
- Text editor (e.g., VS Code)

---

### 📦 Install Required Libraries

Run this command in your terminal to install necessary libraries:

```bash
pip install pycryptodome
```

There are also alternatives that are available intead of `pycryptodome`

But it is recommended, since `pycryptodome` covers all that are needed in this lab

| Library      | Purpose                                                                                 | Use Case in Lab 4                                                |
| ------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| `pycryptodome` | A self-contained Python library for cryptographic functions like AES, RSA, and hashing. | Used for AES encryption, RSA encryption, and digital signatures. |
| `cryptography` | Another popular cryptography library offering secure primitives and recipes.            | Not used in this lab, but it's an alternative to pycryptodome.   |
| `rsa`          | A lightweight Python module focused only on RSA encryption/decryption and signing.      | Also not used here, since pycryptodome already covers RSA.       |
| `hashlib`      | Hashing (SHA-256, SHA-512, etc.)                                                        | Not Used, bust also an alternative for hashing                   |
| `PyNaCl`       | Encryption, signatures using libsodium                                                  | Limited to Ed25519, Curve25519 (not RSA)                         |

<br></br>

---
---

## 🔐 Task 1: Symmetric Encryption (AES)

✅ What You’ll Do

---

📜 Code T1

```py
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_decrypt_user_input():
    key = get_random_bytes(32)  # AES-256
    cipher = AES.new(key, AES.MODE_CBC)

    plaintext = input("Enter a message to encrypt using AES: ").encode()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = cipher.iv

    # Decrypt
    decipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

    print(f"\nEncrypted (hex): {ciphertext.hex()}")
    print(f"Decrypted: {decrypted.decode()}")

aes_encrypt_decrypt_user_input()
```

### 🧠 Explanation for AES

- Uses the same key for both encryption and decryption.
- AES-256 with CBC mode provides strong confidentiality.
- CBC mode uses an IV (Initialization Vector) for randomness.
- Proper padding is needed to handle messages of different lengths.
- Real-world use: VPNs, encrypted file storage.

<br></br>

---
---

## 🔑 Task 2: Asymmetric Encryption (RSA) | Rivest-Shamir-Adleman

✅ What You’ll Do

---

📜 Code T2

```py
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
```

### 🧠 Explanation for RSA

- Uses two keys: public key (encrypt) and private key (decrypt).
- Safer for communication since private key is kept secret.
- OAEP padding adds security against chosen ciphertext attacks.
- Real-world use: SSL/TLS, secure emails (PGP), key exchange.

<br></br>

---
---

## 🧮 Task 3: Hashing with SHA-256

✅ What You’ll Do

---

📜 Code T3

```py
import hashlib  

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
```

🧠 Explanation

- One-way function: cannot retrieve the original input.
- Produces a fixed 256-bit hash value for any input.
- Sensitive to changes (even a 1-letter change makes a big difference).
- Real-world use: password hashing, data integrity, blockchain.

<br></br>

---
---

## ✍️ Task 4: Digital Signatures with RSA

✅ What You’ll Do

---

📜 Code T4

```py
from Crypto.PublicKey import RSA  
from Crypto.Signature import pkcs1_15  
from Crypto.Hash import SHA256  

def digital_signature_user_input():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    message = input("Enter a message to digitally sign: ").encode()
    hash_obj = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash_obj)
    print(f"\n✅ Digital Signature (hex): {signature.hex()}")

    choice = input("\nDo you want to tamper with the message before verification? (yes/no): ").lower()
    if choice == 'yes':
        tampered_message = input("Enter a DIFFERENT (fake) message to simulate tampering: ").encode()
    else:
        tampered_message = message

    tampered_hash = SHA256.new(tampered_message)
    verifier = pkcs1_15.new(RSA.import_key(public_key))
    try:
        verifier.verify(tampered_hash, signature)
        print("✅ Signature is valid. The message has not been changed.")
    except (ValueError, TypeError):
        print("❌ Signature is invalid. The message may have been tampered.")

digital_signature_user_input()
```

🧠 Explanation

- Ensures message authenticity and integrity.
- Signed using private key, verified using public key.
- Combines RSA and SHA-256: hash the message, then sign the hash.
- Real-world use: document signing, certificates, software verification.

## 🧠 Key Concepts Summary Table

| Task              | Algorithm | Key Type         | Purpose                     | Real-world Use Case            |
|-------------------|-----------|------------------|-----------------------------|--------------------------------|
| Symmetric (AES)   | AES-256   | Same key         | Confidentiality             | VPNs, file encryption          |
| Asymmetric (RSA)  | RSA-2048  | Public/Private   | Secure message exchange     | TLS, encrypted email           |
| Hashing (SHA-256) | SHA-256   | None             | Data integrity check        | Passwords, blockchains         |
| Digital Signature | RSA + SHA | Private/Public   | Authentication & Integrity  | E-signatures, software signing |

---
---
