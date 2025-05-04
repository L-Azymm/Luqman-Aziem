import hashlib

def sha256_demo():
    msg1 = b"Hello Lab 4"
    msg2 = b"Hello Lab 4 Modified"

    hash1 = hashlib.sha256(msg1).hexdigest()
    hash2 = hashlib.sha256(msg2).hexdigest()

    print("Hash 1:", hash1)
    print("Hash 2:", hash2)

sha256_demo()
