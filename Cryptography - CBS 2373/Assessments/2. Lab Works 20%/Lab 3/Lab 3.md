# Lab 3: Cryptographic Tools Exploration  

---

## Task 1: Symmetric Encryption with AES (3 marks)

### Steps & Commands

1. **Create sample file**  

   ```sh
   echo "Secret message using AES encryption by Aziem" > secret.txt
   ```

   Change the context to your own

2. **Encrypt with AES-256-CBC**

    ```sh
    openssl enc -aes-256-cbc -salt -in rahsia.txt -out rahsia.enc
    ```

    Enter password when prompted

3. **Decrypt the file**

    ```sh
    openssl enc -d -aes-256-cbc -in rahsia.enc -out rahsia_decrypted.txt
    ```

4. **Verify integrity**

    ```sh
    diff rahsia.txt rahsia_decrypted.txt
    ```

## Task 2: Asymmetric Encryption with RSA (4 marks)
