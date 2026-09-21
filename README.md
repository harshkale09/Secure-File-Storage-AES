# Secure File Storage System with AES-256 & Integrity Verification

A lightweight, CLI-based secure file vault built in Python. This system provides end-to-end symmetric encryption using **AES-256 (Fernet)**, automatically stores encryption metadata, and performs **SHA-256 cryptographic hash checks** during decryption to detect file tampering.

---

## Technical Architecture & Security Flowchart

```mermaid
graph TD
    A[Original File: secret.txt] --> B[Calculate SHA-256 Hash]
    B --> C[Store Hash in metadata.json]
    A --> D[AES-256 Encryption Engine]
    D --> E[Encrypted File: secret.txt.enc]
    
    subgraph Decryption & Verification
        E --> F[AES-256 Decryption Engine]
        F --> G[Decrypted File: decrypted_secret.txt]
        G --> H[Re-calculate SHA-256 Hash]
        C --> I{Compare Hashes}
        H --> I
        I -- Match --> J[VERIFIED: File Untampered]
        I -- Mismatch --> K[CRITICAL: Tampering Detected]
    end
