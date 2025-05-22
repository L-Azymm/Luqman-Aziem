# 🛡️ Lab 4 DUO: Cryptographic Algorithms in Python – RSA Secure Messaging & Digital Signatures (Partner-Based)

This lab demonstrates how to exchange encrypted messages and verify digital signatures using **RSA encryption** in Python. You'll be working with a partner to simulate a real-world secure communication.

No worries if you're not a coding expert — follow each step carefully and everything will work fine!

---

## 👥 Overview

You and your partner will:

1. Generate RSA keys
2. Send and receive encrypted messages
3. Sign a message digitally
4. Verify the digital signature

---

## 🔧 Tools Needed

- Python 3
- `pycryptodome` library (install it using `pip install pycryptodome`)
- Text editor or IDE (VS Code, Thonny, etc.)
- USB, Telegram, or email to share files

---

## 🔐 TASK 1 : Secure Messaging with RSA Encryption

### ✅ STEP 1: Generate Your RSA Key Pair

You’ll create your own private and public key files.

```python
from Crypto.PublicKey import RSA

# Generate 2048-bit RSA key
rsa_key = RSA.generate(2048)

# Export private and public keys
private_key = rsa_key.export_key()
public_key = rsa_key.publickey().export_key()

# Save the keys to files
with open("my_public.pem", "wb") as f:
    f.write(public_key)
with open("my_private.pem", "wb") as f:
    f.write(private_key)
````

📤 **Send your `my_public.pem` to your partner** so they can use it to encrypt a message.

---

### ✅ STEP 2: Partner Encrypts a Secret Message

Your partner uses your public key to lock a message only **you** can unlock.

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load the public key received from partner
with open("partner_public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Write the secret message
message = "Hello! This is a secret message from your partner."
cipher = PKCS1_OAEP.new(public_key)
encrypted = cipher.encrypt(message.encode())

# Save the encrypted message
with open("message.enc", "wb") as f:
    f.write(encrypted)
```

📤 **Send the `message.enc` file back to your partner**.

---

### ✅ STEP 3: Decrypt Message with Private Key

Only you can unlock the message using your private key.

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Load your private key
with open("my_private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Load the encrypted message
with open("message.enc", "rb") as f:
    encrypted_msg = f.read()

# Decrypt the message
cipher = PKCS1_OAEP.new(private_key)
decrypted = cipher.decrypt(encrypted_msg)

print("Decrypted message:", decrypted.decode())
```

✅ You should now see the secret message your partner sent!

---

## ✍️ TASK 2: Digital Signatures

You’ll now **sign** a message with your private key, and your partner will **verify** it with your public key.

---

### ✅ STEP 4: Sign a Message (You)

This proves that a message came from you and was not altered.

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Your message
message = b"This is a signed message."

# Create a hash of the message
hash_msg = SHA256.new(message)

# Load your private key
with open("my_private.pem", "rb") as f:
    private_key = RSA.import_key(f.read())

# Sign the hash
signature = pkcs1_15.new(private_key).sign(hash_msg)

# Save both the message and signature
with open("signed_message.txt", "wb") as f:
    f.write(message)
with open("signature.sig", "wb") as f:
    f.write(signature)
```

📤 **Send `signed_message.txt`, `signature.sig`, and your `my_public.pem` to your partner**.

---

### ✅ STEP 5: Verify the Signature (Partner Side)

Your partner checks if the message truly came from you.

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Load the message, signature, and public key
with open("signed_message.txt", "rb") as f:
    message = f.read()
with open("signature.sig", "rb") as f:
    signature = f.read()
with open("partner_public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

# Hash the message
hash_msg = SHA256.new(message)

# Try to verify the signature
try:
    pkcs1_15.new(public_key).verify(hash_msg, signature)
    print("✅ Signature is valid. Message is authentic.")
except (ValueError, TypeError):
    print("❌ Signature is invalid or tampered.")
```

✅ If it shows **Signature is valid**, then the message is safe and from you!

---

## 🔁 Summary – What to Exchange

| File Name            | Who Sends It | What It’s For                       |
| -------------------- | ------------ | ----------------------------------- |
| `my_public.pem`      | You          | Partner uses this to encrypt/verify |
| `message.enc`        | Partner      | You decrypt with your private key   |
| `signed_message.txt` | You          | Partner checks the original message |
| `signature.sig`      | You          | Partner verifies your digital ID    |

---
---
