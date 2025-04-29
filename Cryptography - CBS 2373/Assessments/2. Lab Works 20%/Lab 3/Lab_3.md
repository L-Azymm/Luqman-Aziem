
# **Lab 3: Hands-on Exploration of Cryptographic Tools**

---

## **Table of Contents**

- [Objectives](#objectives)  
- [Task 1: AES Symmetric Encryption](#task-1-aes-symmetric-encryption)  
- [Task 2: RSA Asymmetric Encryption](#task-2-rsa-asymmetric-encryption)  
- [Task 3: SHA-256 Hashing](#task-3-sha-256-hashing)  
- [Task 4: Digital Signatures](#task-4-digital-signatures)  

---

## **Objectives**

- Learn how to use OpenSSL for encryption and decryption using AES (symmetric) and RSA (asymmetric).
- Understand how to hash data using SHA-256 to check integrity.
- Learn to sign a file digitally using a private key and verify it using a public key.

---

## **Task 1: AES Symmetric Encryption**

**Objective:** Encrypt and decrypt a file using AES-256-CBC mode (symmetric encryption).

---

### Step 1: Create a file

```sh
echo "Secret Message from Zymm to unknown" > secret.txt
```

✅ This creates a new file called `secret.txt` containing a secret message.

---

### Step 2: Encrypt the file

```sh
openssl enc -aes-256-cbc -salt -in secret.txt -out secret.enc
```

✅ Encrypts the file using AES-256 in CBC mode. You will be asked to enter a password to secure the file. The encrypted file will be saved as `secret.enc`.

---

### Step 3: Decrypt the file

```sh
openssl enc -aes-256-cbc -d -in secret.enc -out secret-decrypted.txt
```

✅ Decrypts the `secret.enc` file using the same password and outputs the result into `secret-decrypted.txt`.

---

### Step 4: View and compare the result

```sh
cat secret-decrypted.txt
```

✅ This displays the decrypted message to confirm that it matches the original text.

---

### Explanation

- AES is a symmetric algorithm, meaning the same password is used for both encryption and decryption.
- The `-salt` option adds randomness to the encryption for better security.
- CBC (Cipher Block Chaining) mode encrypts data in blocks, where each block depends on the previous one.

<br><br>

---
---

## **Task 2: RSA Asymmetric Encryption**

**Objective:** Encrypt and decrypt a message using a public/private key pair.

---

### Step 1: Generate a private key

```sh
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
```

✅ This command generates a 2048-bit RSA private key and saves it in `private.pem`.

---

### Step 2: Extract the public key

```sh
openssl rsa -pubout -in private.pem -out public.pem
```

✅ Takes the private key and generates the corresponding public key, saving it to `public.pem`.

---

### Step 3: Create a message file

```sh
echo "This is a secret message" > message.txt
```

✅ This creates a file `message.txt` with the content that we want to encrypt.

---

### Step 4: Encrypt the message with the public key

```sh
openssl rsautl -encrypt -inkey public.pem -pubin -in message.txt -out message.enc
```

✅ Encrypts `message.txt` using the **public key**, saving the output as `message.enc`.

---

### Step 5: Decrypt the message with the private key

```sh
openssl rsautl -decrypt -inkey private.pem -in message.enc -out message-decrypted.txt
```

✅ Decrypts `message.enc` using the **private key** and stores the result in `message-decrypted.txt`.

---

### Step 6: View the decrypted message

```sh
cat message-decrypted.txt
```

✅ This shows the decrypted message. It should match the original message.

---

### Explanation

- RSA uses **two keys**: one public (to encrypt), and one private (to decrypt).
- Public key can be shared freely, but private key must be kept secret.
- Useful for secure communication between two parties.

<br><br>

---
---

## **Task 3: SHA-256 Hashing**

**Objective:** Use SHA-256 hashing to ensure data integrity.

---

### Step 1: Create a simple file

```bash
echo "Luqman Aziem | 123456" > black.txt
```

✅ This makes a file with some login-like info.

---

### Step 2: Hash the file

```bash
openssl dgst -sha256 black.txt
```

✅ Generates a SHA-256 hash of the file content.

---

### Step 3: Change the file slightly

```bash
echo " " >> black.txt
```

✅ Adds just a space at the end of the file.

---

### Step 4: Hash it again

```bash
openssl dgst -sha256 black.txt
```

✅ Hash value will now be completely different.

---

### Explanation

- Even a small change (like a space) causes a **completely different hash**.
- This is called the **avalanche effect**.
- Hashes are used to check **if data has been changed**.

<br><br>

---
---

## **Task 4: Digital Signatures**

**Objective:** Sign a file using a private key and verify the signature using a public key.

---

### Step 1: Create a file to sign

```bash
echo "Digital signature test file" > sign.txt
```

✅ Prepares the file we want to sign.

---

### Step 2: Sign the file with private key

```bash
openssl dgst -sha256 -sign private.pem -out sign.sha256 sign.txt
```

✅ Signs `sign.txt` using SHA-256 and your private key. Signature saved in `sign.sha256`.

---

### Step 3: Verify the signature using public key

```bash
openssl dgst -sha256 -verify public.pem -signature sign.sha256 sign.txt
```

✅ This checks the signature with the public key. It should return **"Verified OK"** if file is untouched.

---

### Step 4: Tamper with the file

```bash
echo "Tampered!" >> sign.txt
```

✅ Changes the content of the signed file.

---

### Step 5: Verify again

```bash
openssl dgst -sha256 -verify public.pem -signature sign.sha256 sign.txt
```

❌ This time the result will say **"Verification Failure"**, because the file was changed.

---

### Explanation

- A digital signature proves that a file **came from the right person** (authenticity) and **was not changed** (integrity).
- Signing is done with the **private key**, and checking is done using the **public key**.
- If the file changes even slightly, the signature will no longer be valid.

---
---
