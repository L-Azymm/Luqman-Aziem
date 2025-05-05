# 🛡️ Lab 4: Cryptographic Algorithms in Python

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
pip install pycryptodome cryptography rsa
```

| Library      | Purpose                                                                                 | Use Case in Lab 4                                                |
| ------------ | --------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| pycryptodome | A self-contained Python library for cryptographic functions like AES, RSA, and hashing. | Used for AES encryption, RSA encryption, and digital signatures. |
| cryptography | Another popular cryptography library offering secure primitives and recipes.            | Not used in this lab, but it's an alternative to pycryptodome.   |
| rsa          | A lightweight Python module focused only on RSA encryption/decryption and signing.      | Also not used here, since pycryptodome already covers RSA.       |

Or you can just run

```bash
pip install pycryptodome
```

Since `pycryptodome` covers all that are needed in this lab

---
---

## 🔐 Task 1: Symmetric Encryption (AES)

✅ What You’ll Do

---

📜 Code T1

### 🧠 Explanation for AES

- Uses the same key for both encryption and decryption.
- AES-256 with CBC mode provides strong confidentiality.
- CBC mode uses an IV (Initialization Vector) for randomness.
- Proper padding is needed to handle messages of different lengths.
- Real-world use: VPNs, encrypted file storage.

---
---

## 🔑 Task 2: Asymmetric Encryption (RSA) | Rivest-Shamir-Adleman

✅ What You’ll Do

---

📜 Code T2

### 🧠 Explanation for RSA

- Uses two keys: public key (encrypt) and private key (decrypt).
- Safer for communication since private key is kept secret.
- OAEP padding adds security against chosen ciphertext attacks.
- Real-world use: SSL/TLS, secure emails (PGP), key exchange.

---
---

## 🧮 Task 3: Hashing with SHA-256

✅ What You’ll Do

---

📜 Code T3

🧠 Explanation

- One-way function: cannot retrieve the original input.
- Produces a fixed 256-bit hash value for any input.
- Sensitive to changes (even a 1-letter change makes a big difference).
- Real-world use: password hashing, data integrity, blockchain.

---
---

## ✍️ Task 4: Digital Signatures with RSA

✅ What You’ll Do

---

📜 Code T4

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
