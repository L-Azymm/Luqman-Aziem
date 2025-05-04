from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

def signature_demo():
    key = RSA.generate(2048)
    private = key
    public = key.publickey()

    message = b"Important Document"
    hash_obj = SHA256.new(message)

    signature = pkcs1_15.new(private).sign(hash_obj)

    try:
        pkcs1_15.new(public).verify(hash_obj, signature)
        print("Signature is valid ✅")
    except (ValueError, TypeError):
        print("Signature is invalid ❌")

signature_demo()
