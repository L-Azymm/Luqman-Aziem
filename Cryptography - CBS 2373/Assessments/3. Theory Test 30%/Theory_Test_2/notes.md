
# ✅ **Theory Test 2 – Study Guide**

---

## 1. **Modern Cryptography Basics**

* **Confidentiality** – Only the right person can read the data.
* **Integrity** – Data has not been changed.
* **Authentication** – Verifying identity.
* **Non-repudiation** – Proof that someone did something (e.g., signed a message).

---

## 2. **Key Terms**

| **Term**              | **Meaning**                                                  |
| --------------------- | ------------------------------------------------------------ |
| **Encryption**        | Turning plaintext into unreadable ciphertext                 |
| **Decryption**        | Turning ciphertext back to plaintext                         |
| **Plaintext**         | Original readable data                                       |
| **Ciphertext**        | Encrypted (scrambled) data                                   |
| **Key**               | Secret value used for encryption/decryption                  |
| **Hash**              | One-way function that creates a fixed output                 |
| **Digital Signature** | Used to verify who sent a message and that it wasn’t changed |

---

## 3. **Symmetric vs Asymmetric**

| **Symmetric**                   | **Asymmetric**                                            |
| ------------------------------- | --------------------------------------------------------- |
| Uses **one key**                | Uses **two keys** (public & private)                      |
| Same key to encrypt and decrypt | Public key encrypts, private key decrypts (or vice versa) |
| Fast                            | Slower                                                    |
| Example: AES                    | Example: RSA                                              |

---

## 4. **Private vs Public Key Usage**

| **Scenario**          | **Key Used for What**                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------- |
| **Encryption**        | Sender uses **recipient’s public key** to encrypt. Only recipient can decrypt using **private key**. |
| **Digital Signature** | Sender signs with **private key**. Receiver verifies with sender’s **public key**.                   |

---

## 5. **Hashing & Digital Signature Concepts**

* Hashing is **one-way**: cannot reverse it.
* SHA-256 is a common hashing algorithm.
* A digital signature = hash of the message + encrypted with sender’s **private key**.
* Digital signatures prove **authenticity** and **integrity**.

---

## 6. **Lab 3 Theory Recap** (no code)

* Focus: Symmetric encryption (AES)
* What you did:

  * Encrypted plaintext using AES with a key
  * Decrypted the ciphertext back
  * Learned that **same key** is used both ways
* Key point: AES is **symmetric**, secure, and fast

---

## 7. **Lab 4 Theory Recap** (no code)

* Focus: RSA & SHA-256
* What you did:

  * Encrypted data using RSA (asymmetric)
  * Created hash using SHA-256
  * Signed data using RSA digital signature
  * Verified that signature matches the data
* Key point: RSA uses **key pair**, and signatures provide **integrity & authenticity**

---

## 8

| **Topic**               | **Key Points**                                                            |
| ----------------------- | ------------------------------------------------------------------------- |
| Brute Force on SSH      | Used Hydra to brute-force login, showed how weak passwords can be cracked |
| Sniffing FTP            | Captured FTP credentials using Wireshark, showed lack of encryption       |
| RSA & Digital Signature | Signed a message, verified signature, explained RSA key roles             |
| AES Encryption          | Encrypted and decrypted a message using AES                               |
| Telnet Attack           | Brute-force Telnet, showed unsecure login over plaintext                  |
| Hash Collision Demo     | Showed different data giving same hash using weak hash functions          |

---
