from Crypto.PublicKey import RSA  
from Crypto.Signature import pkcs1_15  
from Crypto.Hash import SHA256  

def digital_signature_user_input():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    message = input("Enter a message to digitally sign: ").encode()
    hash_obj = SHA256.new(message)
    signature = pkcs1_15.new(key).sign(hash_obj)
    print(f"\n✅ Digital Signature (hex): {signature.hex()}")

    choice = input("\nDo you want to tamper with the message before verification? (yes/no): ").lower()
    if choice == 'yes':
        tampered_message = input("Enter a DIFFERENT (fake) message to simulate tampering: ").encode()
    else:
        tampered_message = message

    tampered_hash = SHA256.new(tampered_message)
    verifier = pkcs1_15.new(RSA.import_key(public_key))
    try:
        verifier.verify(tampered_hash, signature)
        print("✅ Signature is valid. The message has not been changed.")
    except (ValueError, TypeError):
        print("❌ Signature is invalid. The message may have been tampered.")

digital_signature_user_input()
