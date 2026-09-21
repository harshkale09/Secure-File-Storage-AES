import os
import json
import hashlib
from datetime import datetime
from cryptography.fernet import Fernet

KEY_FILE = "secret.key"
METADATA_FILE = "metadata.json"

# 1. Key Management
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as k_file:
            return k_file.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as k_file:
            k_file.write(key)
        print("[+] New AES encryption key generated and saved to 'secret.key'.")
        return key

# 2. SHA-256 Hash Calculation for Integrity Check
def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

# 3. Metadata Storage
def save_metadata(enc_filename, original_filename, orig_hash, timestamp):
    metadata = {}
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, "r") as m_file:
            try:
                metadata = json.load(m_file)
            except json.JSONDecodeError:
                metadata = {}
    
    metadata[enc_filename] = {
        "original_filename": original_filename,
        "sha256_hash": orig_hash,
        "timestamp": timestamp
    }
    
    with open(METADATA_FILE, "w") as m_file:
        json.dump(metadata, m_file, indent=4)

# 4. File Encryption Engine
def encrypt_file(file_path, cipher):
    if not os.path.exists(file_path):
        print(f"[!] File '{file_path}' not found!")
        return

    orig_hash = calculate_sha256(file_path)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, "rb") as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data)
    enc_filename = file_path + ".enc"

    with open(enc_filename, "wb") as f:
        f.write(encrypted_data)

    save_metadata(enc_filename, file_path, orig_hash, timestamp)
    print(f"[SUCCESS] File encrypted and saved as '{enc_filename}'")
    print(f"[*] Original SHA-256 Hash recorded: {orig_hash}")

# 5. File Decryption Engine & Tamper Check
def decrypt_file(enc_file_path, cipher):
    if not os.path.exists(enc_file_path):
        print(f"[!] Encrypted file '{enc_file_path}' not found!")
        return

    if not os.path.exists(METADATA_FILE):
        print("[!] Metadata database missing!")
        return

    with open(METADATA_FILE, "r") as m_file:
        metadata = json.load(m_file)

    file_meta = metadata.get(enc_file_path)
    if not file_meta:
        print("[!] No metadata record found for this file!")
        return

    with open(enc_file_path, "rb") as f:
        encrypted_data = f.read()

    try:
        decrypted_data = cipher.decrypt(encrypted_data)
    except Exception:
        print("[!] Decryption failed! Key mismatch or corrupted file.")
        return

    dec_filename = "decrypted_" + os.path.basename(file_meta["original_filename"])
    with open(dec_filename, "wb") as f:
        f.write(decrypted_data)

    # Hash Integrity Verification
    new_hash = calculate_sha256(dec_filename)
    original_hash = file_meta["sha256_hash"]

    print(f"[SUCCESS] File decrypted and saved as '{dec_filename}'")
    print("\n--- Integrity Verification ---")
    print(f"Original Hash:  {original_hash}")
    print(f"Decrypted Hash: {new_hash}")

    if new_hash == original_hash:
        print("[VERIFIED] Integrity Intact: Hashes MATCH perfectly! File has NOT been tampered with.")
    else:
        print("[CRITICAL] TAMPERING DETECTED: Hashes DO NOT match! File was altered.")

# 6. Interactive CLI Interface
def main():
    key = load_or_generate_key()
    cipher = Fernet(key)

    while True:
        print("\n==========================================")
        print("  AES-256 SECURE FILE STORAGE SYSTEM")
        print("==========================================")
        print("1. Encrypt a File")
        print("2. Decrypt a File & Verify Integrity")
        print("3. Exit")
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            filename = input("Enter the file name to encrypt (e.g., secret.txt): ").strip()
            encrypt_file(filename, cipher)
        elif choice == "2":
            filename = input("Enter encrypted file name (e.g., secret.txt.enc): ").strip()
            decrypt_file(filename, cipher)
        elif choice == "3":
            print("Exiting Secure Vault. Stay safe!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()