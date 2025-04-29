# Study for Theory Test 1 (Cryptography)

## 1. Modern Cryptography Basics

- **Cryptography: Securing information by transforming it into an unreadable format, so that only authorized parties can understand it**

- **Key Terms**

  - `Encryption`: Turning plaintext into ciphertext.

  - `Decryption`: Turning ciphertext back into plaintext.
  - `Key`: A secret value used to encrypt or decrypt data.
  - `Plaintext`: Original readable data.
  - `Ciphertext`: Data that has been encrypted and is unreadable.
  - `Cipher`: The method (algorithm) used for encryption and decryption.
  - `Encoding`: Changing data format for storage or transmission (not for hiding).
  - `Passphrase`: A password used to protect a key.
  - `Symmetric Encryption`: Using the same key to encrypt and decrypt.
  - `Asymmetric Encryption`: Using different keys to encrypt and decrypt.
  - `Brute Force`: Trying all possible passwords or keys until the correct one is found.
  - `Cryptanalysis`: Finding weaknesses in encryption to break it without guessing.

## 2.Symmetric vs Asymmetric Cryptography

| Aspect             | Symmetric Cryptography                   | Asymmetric Cryptography                 |
| ------------------ | ---------------------------------------- | --------------------------------------- |
| Keys Used          | Same key for encryption and decryption   | Different keys (public and private)     |
| Speed              | Faster                                   | Slower                                  |
| Example Algorithms | AES, DES                                 | RSA, ECC                                |
| Use Case           | Encrypting large amounts of data quickly | Secure key exchange, digital signatures |
| Key Sharing        | Key must be shared secretly              | Public key can be shared openly         |

**When to use:**

- `Symmetric`: When you and the receiver already share a secret key.
- `Asymmetric`: When you need to securely exchange information without a shared secret

## 3.Private vs Public Key (Encryption/Decryption vs Digital Signatures)

### Encryption/Decryption

- Public Key Encryption:
  - Encrypt with public key, decrypt with private key.
  - Anyone can encrypt a message to you, but only you (with the private key) can decrypt it.

### Digital Signatures

- Sign with private key, verify with public key.

  - You create a signature with your private key (proving it was you).
  - Anyone with your public key can verify that the message was signed by you

- Purpose Encryption Digital Signature
  - Goal Confidentiality Authentication, Integrity, Non-repudiation
  - Process Encrypt with public key, decrypt with private key Sign with private key, verify with public key

| Purpose | Encryption                                        | Digital Signature                             |
| ------- | ------------------------------------------------- | --------------------------------------------- |
| Goal    | Confidentiality                                   | Authentication, Integrity, Non-repudiation    |
| Process | Encrypt with public key, decrypt with private key | Sign with private key, verify with public key |

## Lab Notes

### Lab 3: Public Key Infrastructure (PKI)

- `PKI`: A system for managing public keys and digital certificates.
- `Certificate`: A file that proves a public key belongs to a person or organization.
- `Certificate` Authority (CA): A trusted third party that issues certificates.
- `Key Pair`: A public key (shared with others) and a private key (kept secret).
- `Trust`: Built through CAs—if you trust the CA, you trust the certificate.

### Lab 4: Secure Key Exchange

- `Key Exchange`: The process of sharing encryption keys securely.
- `Diffie-Hellman`: A method for two people to create a shared secret key, even if the communication channel is not secure.
- `Shared Secret`: A key that both parties know but no one else does.
- `Why It Matters`: If the key exchange isn’t secure, attackers can steal the key and read your encrypted data.
