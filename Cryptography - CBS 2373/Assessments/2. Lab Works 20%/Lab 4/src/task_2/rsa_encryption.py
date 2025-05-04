from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def rsa_demo():
    key = RSA.generate(2048)
    private = key.export_key()
    public = key.publickey().export_key()

    cipher = PKCS1_OAEP.new(RSA.import_key(public))
    plaintext = b"My RSA Message"
    ciphertext = cipher.encrypt(plaintext)

    decipher = PKCS1_OAEP.new(RSA.import_key(private))
    decrypted = decipher.decrypt(ciphertext)

    print("Original:", plaintext.decode())
    print("Decrypted:", decrypted.decode())

rsa_demo()
