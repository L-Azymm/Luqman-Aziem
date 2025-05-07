from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_encrypt_decrypt_user_input():
    key = get_random_bytes(32) 
    cipher = AES.new(key, AES.MODE_CBC)

    plaintext = input("Enter a message to encrypt using AES: ").encode()
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    iv = cipher.iv


    decipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

    print(f"\nEncrypted (hex): {ciphertext.hex()}")
    print(f"Decrypted: {decrypted.decode()}")

aes_encrypt_decrypt_user_input()
