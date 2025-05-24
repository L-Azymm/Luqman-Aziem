from Crypto.Cipher import AES
from hashlib import sha256
import os

KEY_SUFFIX = "RahsiaLagi"
KEY_STR = f"Bukan{KEY_SUFFIX}"
KEY = sha256(KEY_STR.encode()).digest()[:16]

def unpad(data):
    pad_len = data[-1]
    if pad_len < 1 or pad_len > 16:
        raise ValueError("Invalid padding length")
    return data[:-pad_len]

def decrypt_file(enc_filepath, output_folder):
    with open(enc_filepath, "rb") as f:
        ciphertext = f.read()

    cipher = AES.new(KEY, AES.MODE_ECB)
    padded_plaintext = cipher.decrypt(ciphertext)
    plaintext = unpad(padded_plaintext)

    os.makedirs(output_folder, exist_ok=True)

    # Remove .enc and add .txt
    base_name = os.path.basename(enc_filepath)
    name_without_ext = base_name.replace(".enc", "")
    new_filename = f"{name_without_ext}.txt"
    dec_filepath = os.path.join(output_folder, new_filename)

    with open(dec_filepath, "wb") as f:
        f.write(plaintext)

    print(f"Decrypted: {enc_filepath} -> {dec_filepath}")

if __name__ == "__main__":
    locked_folder = "locked_files/"
    invaded_folder = "invaded_files/"

    for filename in os.listdir(locked_folder):
        if filename.endswith(".enc"):
            decrypt_file(os.path.join(locked_folder, filename), invaded_folder)
