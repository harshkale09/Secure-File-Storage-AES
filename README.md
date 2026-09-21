# Secure File Storage System with AES-256 & Integrity Verification

A lightweight, CLI-based secure file vault built in Python. This system provides end-to-end symmetric encryption using **AES-256 (Fernet)**, automatically stores encryption metadata, and performs **SHA-256 cryptographic hash checks** during decryption to detect file tampering.

---

## Key Features

- **AES-256 Cryptographic Protection**: Uses authenticated symmetric encryption to secure confidential files.
- **SHA-256 Integrity Verification**: Calculates and verifies cryptographic checksums to detect file alteration/tampering.
- **Structured Metadata Management**: Logs file names, SHA-256 hashes, and timestamp records in a local JSON database.
- **Key Security & Management**: Automatically manages symmetric encryption keys (`secret.key`).

---

## Technical Architecture
