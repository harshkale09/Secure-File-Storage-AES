# 🔐 Secure File Storage System

A lightweight, CLI-based secure file storage system built with Python.

This project provides secure file encryption using Fernet symmetric encryption and verifies file integrity using SHA-256 hashing. It also maintains file-related metadata in a local JSON file.

---

## 🚀 Key Features

- Secure file encryption using Fernet symmetric encryption
- Automatic encryption key generation and management
- SHA-256 based file integrity verification
- Encrypted .enc file generation
- Metadata storage using JSON
- Integrity checking to identify file modification
- Simple command-line interface (CLI)

---

## 🏗️ Technical Architecture

The system follows a secure file-processing workflow:

                    ┌───────────────────┐
                    │     User Input    │
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌───────────────────┐
                    │ Load / Generate   │
                    │    Secret Key     │
                    └─────────┬─────────┘
                              │
                 ┌────────────┴────────────┐
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │  Encrypt File   │       │  Decrypt File   │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │ Calculate       │       │ Fernet          │
        │ SHA-256 Hash    │       │ Decryption      │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │ Fernet          │       │ Calculate New   │
        │ Encryption      │       │ SHA-256 Hash    │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │ Save .enc File  │       │ Compare Hashes  │
        └────────┬────────┘       └────────┬────────┘
                 │                         │
                 ▼                    ┌────┴────┐
        ┌─────────────────┐            │         │
        │ Save Metadata   │            ▼         ▼
        │ in metadata.json│          MATCH    NO MATCH
        └─────────────────┘            │         │
                                       ▼         ▼
                                   VERIFIED   POSSIBLE
                                              TAMPERING

---

## 🔑 Key Management

When the application starts, it checks whether secret.key exists.

If the key already exists, it is loaded and used for encryption and decryption.

If the key does not exist, a new Fernet key is generated and saved.

Key Management Flow:

Application Starts
       ↓
Check secret.key
       ↓
 ┌─────┴─────┐
 │           │
Exists     Missing
 │           │
 ↓           ↓
Load       Generate
Key          Key
 │           │
 └─────┬─────┘
       ↓
Encryption / Decryption

---

## 🔒 File Encryption

When the user selects the encryption operation, the system performs the following steps:

1. The user provides the file path.
2. The application reads the file.
3. A SHA-256 hash is calculated for the original file.
4. The file data is encrypted using Fernet.
5. The encrypted data is saved as an .enc file.
6. File information and the original SHA-256 hash are stored in metadata.json.

Encryption Flow:

Original File
      ↓
Calculate SHA-256
      ↓
Fernet Encryption
      ↓
Encrypted File (.enc)
      ↓
Store Metadata

---

## 🔓 File Decryption & Integrity Verification

When the user selects the decryption and verification operation:

1. The encrypted file is selected.
2. The required metadata is loaded.
3. The encrypted data is decrypted using the Fernet key.
4. A new SHA-256 hash is calculated from the decrypted data.
5. The new hash is compared with the original stored hash.

If both hashes match, the file passes the integrity check.

If the hashes do not match, the system identifies a possible modification or integrity failure.

Verification Flow:

Encrypted File
      ↓
Fernet Decryption
      ↓
Decrypted Data
      ↓
Calculate SHA-256
      ↓
Compare With Stored Hash
      ↓
   ┌──┴───────────┐
   │              │
 MATCH        NO MATCH
   │              │
   ↓              ↓
VERIFIED      INTEGRITY
              FAILURE /
              POSSIBLE
              TAMPERING

---

## 🛡️ SHA-256 Integrity Verification

SHA-256 is used to create a cryptographic hash representation of the file data.

During encryption, the SHA-256 hash of the original file is stored in the metadata.

During verification, a new hash is calculated and compared with the stored value.

Integrity Check Logic:

Original File
      ↓
Original SHA-256
      ↓
Stored in Metadata
      ↓
Decrypted File
      ↓
New SHA-256
      ↓
Compare Both Hashes
      ↓
   ┌──┴─────────────┐
   │                │
 Same             Different
   │                │
   ↓                ↓
Integrity        Possible File
Verified         Modification

---

## 💻 Console / Execution Flow

The application provides a command-line interface for performing the main operations.

Main Menu:

==========================================
     SECURE FILE STORAGE SYSTEM
==========================================
1. Encrypt a File
2. Decrypt a File & Verify Integrity
3. Exit

The user selects the required operation and provides the required file information.

Encryption Execution:

[1] Encrypt a File

Enter file path:
> sample.txt

Processing file...
Calculating SHA-256 hash...
Encrypting file using Fernet...
Saving encrypted file...
Updating metadata...

Encryption process completed.

Decryption & Verification Execution:

[2] Decrypt a File & Verify Integrity

Enter encrypted file path:
> sample.txt.enc

Decrypting file...
Calculating SHA-256 hash...
Loading original hash from metadata...
Comparing hashes...

Integrity verification completed.

Integrity Verification Result:

Original SHA-256 Hash:
<stored hash>

Decrypted File SHA-256 Hash:
<calculated hash>

Hash Comparison:
MATCH → Integrity Verified

If the calculated hash is different:

Original SHA-256 Hash:
<stored hash>

Decrypted File SHA-256 Hash:
<calculated hash>

Hash Comparison:
NO MATCH → Possible File Modification

These console examples describe the execution flow of the application and provide a clear explanation of the project's working during an interview or project demonstration.

---

## 📋 Metadata Management

The system maintains file-related information in metadata.json.

The metadata is used to keep track of information required for integrity verification.

Typical information includes:

- Original filename
- SHA-256 hash
- Timestamp
- Encrypted filename reference

Metadata Workflow:

File
 ↓
Calculate SHA-256
 ↓
Create Metadata
 ↓
metadata.json
 ↓
Used During Verification

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

File Description:

secure_vault.py - Main Python application containing the encryption, decryption and integrity verification logic.

metadata.json - Stores file metadata and SHA-256 information used during verification.

requirements.txt - Contains the Python dependencies required by the project.

secret.key - Stores the generated Fernet encryption key.

README.md - Project documentation.

.gitignore - Used to prevent selected files from being tracked by Git.

---

## 🧰 Technologies Used

- Python 3
- Cryptography / Fernet
- SHA-256
- JSON
- OS File Handling
- Command-Line Interface

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
- Python-based security automation

---

## ⚙️ Installation & Usage

Clone the Repository:

git clone https://github.com/harshkale09/Secure-File-Storage-AES.git

Navigate to the Project:

cd Secure-File-Storage-AES

Install Dependencies:

pip install -r requirements.txt

Run the Application:

python secure_vault.py

After running the application, follow the command-line menu to encrypt or decrypt files and perform integrity verification.

---

## 🎯 Project Objective

The main objective of this project is to demonstrate how file encryption and cryptographic hashing can be combined to protect files and verify their integrity.

The project provides a practical implementation of secure file storage concepts using Python.

---

## 📌 Limitations

This project is developed primarily for educational and cybersecurity learning purposes.

A production-level secure storage system would require additional security controls such as advanced key management, authentication, access control, secure key storage, detailed audit logging and secure deletion mechanisms.

---

## 🔮 Future Improvements

Possible future improvements include:

- Password-based key derivation
- User authentication
- Improved secure key storage
- Multiple-user support
- Graphical user interface
- File selection interface
- Detailed audit logging
- Cloud-based secure storage
- Automated integrity monitoring

---

## 👨‍💻 Author

Harsh Kale

B.Sc. Forensic Science & Cyber Security

GitHub: https://github.com/harshkale09

---

## 📜 Disclaimer

This project was developed for educational and cybersecurity learning purposes.

It demonstrates fundamental concepts of file encryption, cryptographic hashing and file integrity verification.
