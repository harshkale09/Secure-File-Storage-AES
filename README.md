# 🔐 Secure File Storage System

A lightweight, CLI-based secure file storage system built with Python.

This project demonstrates secure file handling using Fernet authenticated symmetric encryption, SHA-256 cryptographic hashing, encryption key management, metadata storage, and file integrity verification.

The system can encrypt files, store their integrity information, decrypt encrypted files, and verify whether the recovered file matches its original SHA-256 hash.

---

## 🚀 Key Features

- 🔒 Secure file encryption using Fernet symmetric encryption
- 🔑 Automatic encryption key generation and management
- 🧮 SHA-256 cryptographic hashing
- 🛡️ File integrity verification
- 🚨 Detection of possible file modification or tampering
- 📦 Encrypted `.enc` file generation
- 📋 Metadata storage using JSON
- 💻 Simple command-line interface (CLI)
- ⚙️ Automated encryption and decryption workflow
- 📝 Timestamp-based metadata recording

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how encryption and cryptographic hashing can be combined to protect files and verify their integrity.

The project focuses on the following security concepts:

- Confidentiality through encryption
- Integrity through SHA-256 hashing
- Secure encryption key handling
- File modification detection
- Metadata-based verification
- Python-based security automation

---

## 🏗️ Technical Architecture

The complete system follows this workflow:

                    ┌─────────────────────┐
                    │      User Input     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Load / Generate Key │
                    │     secret.key      │
                    └──────────┬──────────┘
                               │
                 ┌─────────────┴─────────────┐
                 │                           │
                 ▼                           ▼
        ┌──────────────────┐        ┌──────────────────┐
        │  Encrypt File    │        │  Decrypt File    │
        └────────┬─────────┘        └────────┬─────────┘
                 │                           │
                 ▼                           ▼
        ┌──────────────────┐        ┌──────────────────┐
        │ Calculate        │        │ Fernet           │
        │ SHA-256 Hash     │        │ Decryption       │
        └────────┬─────────┘        └────────┬─────────┘
                 │                           │
                 ▼                           ▼
        ┌──────────────────┐        ┌──────────────────┐
        │ Fernet           │        │ Calculate New    │
        │ Encryption       │        │ SHA-256 Hash     │
        └────────┬─────────┘        └────────┬─────────┘
                 │                           │
                 ▼                           ▼
        ┌──────────────────┐        ┌──────────────────┐
        │ Save .enc File   │        │ Compare Hashes   │
        └────────┬─────────┘        └────────┬─────────┘
                 │                           │
                 ▼                      ┌────┴────┐
        ┌──────────────────┐             │         │
        │ Store Metadata   │             ▼         ▼
        │ in metadata.json │           MATCH    NO MATCH
        └──────────────────┘             │         │
                                         ▼         ▼
                                     VERIFIED   POSSIBLE
                                                MODIFICATION

---

## 🔑 Key Management

The application uses a local Fernet encryption key stored in `secret.key`.

When the application starts, it checks whether the key file already exists.

Key Management Flow:

                    Application Starts
                           │
                           ▼
                    Check secret.key
                           │
                    ┌──────┴──────┐
                    │             │
                 Exists         Missing
                    │             │
                    ▼             ▼
                Load Key     Generate Key
                    │             │
                    └──────┬──────┘
                           │
                           ▼
                  Fernet Cipher Ready
                           │
                  ┌────────┴────────┐
                  ▼                 ▼
              Encryption        Decryption

If `secret.key` does not exist, a new Fernet key is generated and saved automatically.

⚠️ The encryption key is critical. Losing the key can prevent encrypted files from being decrypted.

---

## 🔒 File Encryption Process

When the user selects the encryption option, the system performs the following operations:

1. Accept the input file name.
2. Check whether the file exists.
3. Calculate the original SHA-256 hash.
4. Read the file data.
5. Encrypt the data using Fernet.
6. Create an encrypted `.enc` file.
7. Store the original SHA-256 hash in `metadata.json`.
8. Store the original filename and timestamp.

Encryption Flow:

                 Original File
                       │
                       ▼
                File Existence Check
                       │
                       ▼
                 Calculate SHA-256
                       │
                       ▼
                Read File Data
                       │
                       ▼
               Fernet Encryption
                       │
                       ▼
                Encrypted Data
                       │
                       ▼
                 Save .enc File
                       │
                       ▼
              Update metadata.json

---

## 🔓 File Decryption Process

When the user selects the decryption option:

1. The encrypted file is located.
2. `metadata.json` is loaded.
3. The corresponding metadata record is retrieved.
4. The encrypted data is decrypted using the Fernet key.
5. The decrypted data is saved as a new file.
6. A new SHA-256 hash is calculated.
7. The new hash is compared with the original stored hash.
8. The integrity result is displayed.

Decryption Flow:

                Encrypted File
                       │
                       ▼
                 Load Metadata
                       │
                       ▼
                Fernet Decryption
                       │
                       ▼
                 Decrypted File
                       │
                       ▼
                Calculate SHA-256
                       │
                       ▼
              Compare With Stored Hash
                       │
                 ┌─────┴─────┐
                 │           │
               MATCH      NO MATCH
                 │           │
                 ▼           ▼
             VERIFIED    INTEGRITY
                         FAILURE /
                         POSSIBLE
                         MODIFICATION

---

## 🛡️ SHA-256 Integrity Verification

SHA-256 is used to generate a fixed-length cryptographic representation of the file contents.

The original hash is calculated before encryption and stored in `metadata.json`.

After decryption, the system calculates a new SHA-256 hash from the recovered file.

The two hashes are then compared.

Integrity Verification Flow:

                Original File
                     │
                     ▼
              Original SHA-256
                     │
                     ▼
              Store in Metadata
                     │
                     ▼
               Encrypt File
                     │
                     ▼
              Decrypt File
                     │
                     ▼
               New SHA-256
                     │
                     ▼
               Compare Hashes
                     │
               ┌─────┴─────┐
               │           │
             SAME       DIFFERENT
               │           │
               ▼           ▼
          INTEGRITY     POSSIBLE
           VERIFIED     MODIFICATION

---

## 💻 Console Interface

The application provides an interactive command-line interface.

Main Menu:

==========================================
  AES-256 SECURE FILE STORAGE SYSTEM
==========================================
1. Encrypt a File
2. Decrypt a File & Verify Integrity
3. Exit

Select an option (1-3):

The menu allows the user to encrypt a file, decrypt an encrypted file, verify integrity, or exit the application.

---

## 🔬 Console Execution & Verification

The following examples are based on the actual console messages implemented in `secure_vault.py`.

### 1️⃣ Encryption Execution

User selects:

Select an option (1-3): 1

Enter the file name to encrypt (e.g., secret.txt): sample.txt

Successful execution produces output in this format:

[SUCCESS] File encrypted and saved as 'sample.txt.enc'
[*] Original SHA-256 Hash recorded: <SHA-256 hash>

The encrypted file is created with the `.enc` extension and the original hash is stored in `metadata.json`.

---

### 2️⃣ Successful Decryption & Integrity Verification

User selects:

Select an option (1-3): 2

Enter encrypted file name (e.g., secret.txt.enc): sample.txt.enc

Successful verification produces output in this format:

[SUCCESS] File decrypted and saved as 'decrypted_sample.txt'

--- Integrity Verification ---
Original Hash:  <stored SHA-256 hash>
Decrypted Hash: <calculated SHA-256 hash>

[VERIFIED] Integrity Intact: Hashes MATCH perfectly! File has NOT been tampered with.

This indicates that the SHA-256 hash of the decrypted file matches the original stored hash.

---

## 🚨 Tampering / Modification Detection

The project also contains a security check for file integrity.

The verification logic compares:

Original SHA-256 Hash
              │
              ▼
        Stored Metadata
              │
              ▼
      Decrypted File Hash
              │
              ▼
       Compare Both Values
              │
        ┌─────┴─────┐
        │           │
      MATCH      DIFFERENT
        │           │
        ▼           ▼
    VERIFIED    TAMPERING /
                MODIFICATION
                DETECTED

If the decrypted file produces a different SHA-256 hash from the original stored hash, the application reports:

[CRITICAL] TAMPERING DETECTED: Hashes DO NOT match! File was altered.

This provides an integrity warning when the recovered file content no longer matches the original file recorded during encryption.

### Important Verification Behaviour

If the encrypted file itself is corrupted or modified in a way that causes Fernet authentication to fail, the application can stop earlier and display:

[!] Decryption failed! Key mismatch or corrupted file.

Therefore, the project demonstrates two relevant protection outcomes:

1. Fernet detects invalid/corrupted encrypted data during decryption.
2. SHA-256 comparison detects a mismatch between original and recovered file contents.

---

## 📋 Metadata Management

The project maintains file-related information in:

`metadata.json`

Metadata includes information such as:

- Original filename
- Original SHA-256 hash
- Timestamp
- Encrypted filename reference

Metadata Workflow:

                 File
                   │
                   ▼
            Calculate SHA-256
                   │
                   ▼
             Create Metadata
                   │
                   ▼
             metadata.json
                   │
                   ▼
          Used During Verification

This metadata allows the system to compare the original file integrity information with the decrypted file.

---

## 📂 Project Structure

Secure-File-Storage-AES/
│
├── secure_vault.py
├── metadata.json
├── requirements.txt
├── secret.key
├── README.md
└── .gitignore

### File Description

`secure_vault.py`
Main Python application containing encryption, decryption, key management, metadata handling, and integrity verification logic.

`metadata.json`
Stores original filenames, SHA-256 hashes, and timestamps used for integrity verification.

`requirements.txt`
Contains the Python dependencies required by the project.

`secret.key`
Stores the generated Fernet encryption key locally.

`README.md`
Project documentation.

`.gitignore`
Used to prevent selected sensitive or unnecessary files from being tracked by Git.

---

## 🧰 Technologies Used

- Python 3
- Cryptography Library
- Fernet Symmetric Encryption
- SHA-256
- JSON
- OS File Handling
- Command-Line Interface (CLI)

---

## 🔐 Security Concepts Demonstrated

This project demonstrates practical understanding of:

- Symmetric encryption
- Encryption key management
- Cryptographic hashing
- File integrity verification
- File modification detection
- Secure file handling
- Metadata management
- Exception handling
- Python security automation
- Command-line security tooling

---

## ⚙️ Installation & Usage

### Clone the Repository

git clone https://github.com/harshkale09/Secure-File-Storage-AES.git

### Navigate to the Project

cd Secure-File-Storage-AES

### Install Dependencies

pip install -r requirements.txt

### Run the Application

python secure_vault.py

### Basic Usage

1. Run the application.
2. Select option `1` to encrypt a file.
3. Enter the file name.
4. The encrypted `.enc` file and metadata are generated.
5. Select option `2` to decrypt and verify the file.
6. Compare the displayed integrity result.
7. Select option `3` to exit.

---

## 🧪 Security Testing Scenarios

The project can be tested using the following scenarios:

### Test Case 1 — Normal Encryption

Input:
A valid text file such as `sample.txt`

Expected Result:
- Encrypted `.enc` file is created.
- SHA-256 hash is calculated.
- Metadata is updated.

### Test Case 2 — Normal Decryption

Input:
A valid encrypted `.enc` file and matching key.

Expected Result:
- File is decrypted successfully.
- New SHA-256 hash is calculated.
- Hashes match.
- Integrity is verified.

### Test Case 3 — Invalid or Corrupted Encrypted File

Input:
A corrupted or incompatible encrypted file.

Expected Result:

[!] Decryption failed! Key mismatch or corrupted file.

### Test Case 4 — Integrity Mismatch

Input:
A decrypted file whose contents no longer correspond to the original stored SHA-256 value.

Expected Result:

[CRITICAL] TAMPERING DETECTED: Hashes DO NOT match! File was altered.

---

## ⚠️ Security Considerations

This project is intended for educational and cybersecurity learning purposes.

Important considerations:

- The `secret.key` file must be protected.
- Anyone who obtains the encryption key may be able to decrypt protected files.
- `metadata.json` contains integrity-related information and should also be protected.
- This project does not implement user authentication or role-based access control.
- A production-grade secure storage system would require stronger key-management architecture and additional security controls.

---

## 📌 Limitations

The current implementation is a learning-focused secure file storage prototype.

Current limitations include:

- Local key storage
- No password-based key derivation
- No user authentication
- No role-based access control
- No secure deletion mechanism
- No detailed audit logging
- No graphical user interface
- No cloud storage integration
- Limited access-control functionality

---

## 🔮 Future Improvements

Possible future improvements include:

- Password-based key derivation
- Secure password authentication
- Improved key storage
- Multi-user support
- Role-based access control
- Graphical user interface
- File selection interface
- Detailed audit logging
- Automated integrity monitoring
- Secure file deletion
- Cloud-based encrypted storage
- Improved security event logging

---

## 🧠 What This Project Demonstrates

By completing this project, the following cybersecurity concepts are practically demonstrated:

File
 ↓
Hash
 ↓
Encryption
 ↓
Secure Storage
 ↓
Decryption
 ↓
New Hash
 ↓
Hash Comparison
 ↓
Integrity Result

The project combines confidentiality and integrity concepts into a practical Python-based security tool.

---

## 📊 Project Workflow Summary

                    ┌────────────────────┐
                    │     INPUT FILE     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   SHA-256 HASH     │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ FERNET ENCRYPTION │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   ENCRYPTED .ENC   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │   METADATA.JSON    │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │      DECRYPT       │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ NEW SHA-256 HASH   │
                    └─────────┬──────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │  COMPARE HASHES    │
                    └─────────┬──────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                 MATCH              DIFFERENT
                    │                   │
                    ▼                   ▼
               VERIFIED          POSSIBLE
                                 MODIFICATION

---

## 🎓 Learning Outcomes

This project helped demonstrate practical understanding of:

- Python file handling
- Symmetric cryptography
- Fernet encryption
- SHA-256 hashing
- Encryption key management
- JSON-based metadata storage
- Integrity verification
- Error handling
- Security-oriented programming
- Command-line application development

---

## 👨‍💻 Author

Harsh Kale

B.Sc. Forensic Science & Cyber Security

GitHub:
https://github.com/harshkale09

Project Repository:
https://github.com/harshkale09/Secure-File-Storage-AES

---

## 📜 Disclaimer

This project was developed for educational and cybersecurity learning purposes.

It demonstrates fundamental concepts of file encryption, cryptographic hashing, key management, and file integrity verification.

It should not be considered a complete production-grade secure storage solution without additional security controls, testing, auditing, and professional security review.
