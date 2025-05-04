from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def aes_demo():
    key = get_random_bytes(32)  # 256-bit key
    cipher = AES.new(key, AES.MODE_CBC)  # CBC mode
    message = b"Cryptography Lab by Your Name, Your ID!"
    
    ciphertext = cipher.encrypt(pad(message, AES.block_size))
    iv = cipher.iv

    decipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(decipher.decrypt(ciphertext), AES.block_size)

    print("Original:", message.decode())
    print("Decrypted:", decrypted.decode())

aes_demo()
