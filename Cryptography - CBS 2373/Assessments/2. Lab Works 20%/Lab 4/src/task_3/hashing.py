import hashlib  

def compute_sha256(data):
    sha = hashlib.sha256()  
    sha.update(data) 
    return sha.hexdigest()

msg1 = input("Enter first message to hash: ").encode() 
msg2 = input("Enter second message to hash: ").encode()

hash1 = compute_sha256(msg1)
hash2 = compute_sha256(msg2)

print(f"\nHash 1: {hash1}")
print(f"Hash 2: {hash2}")

if hash1 == hash2:
    print("✅ Hashes are the same (messages are identical)")
else:
    print("❌ Hashes are different (messages are not the same)")
