# 🔐About Cry(p)Tool — File Encryption & Decryption

A simple but effective Python tool to **encrypt and decrypt any type of file** using **password-based symmetric encryption**.

This project was built as part of my personal journey into cybersecurity, aiming to better understand how encryption works — both for protection and for exploitation.

---

## 🧠 Motivation

Back when I first learned about one of the most impactful cyberattacks in history — **WannaCry** — I became fascinated by how a single ransomware campaign could encrypt thousands of systems worldwide, making files completely inaccessible.

That event made me realize how powerful encryption can be — for good or for harm.

Inspired by that, I decided to test my own skills by writing this simple file encryption and decryption tool. The goal wasn’t just to build something functional, but to truly **understand how attackers think and operate**.

In the end, I realized how **easy it is to misuse these kinds of tools**. That's exactly why it's so important to study them responsibly — because **knowing how attacks happen is the first step to defending against them**.

This project is a reminder that learning offensive techniques should always go hand in hand with ethical responsibility.

---

## 📜 About the Project

-  **Encrypt and decrypt any file type** (PDF, images, documents, videos, zip files, ISO, etc.).
-  Password-based encryption.
-  Uses **AES encryption under the hood** with **Fernet** (symmetric authenticated cryptography).

---
Python
## 🧠 How It Works

- Your password is converted into a **SHA-256 hash**, then encoded in **Base64** to create a key compatible with the **Fernet** encryption algorithm.
- The tool supports both **encryption** and **decryption** using that password-derived key.
- Files are read in binary mode and processed entirely in memory.

⚠️ **Note:** For very large files (several gigabytes), this script may consume significant memory since it reads the entire file at once. If needed, it can be refactored to process files in chunks.

---

## ⚙️ Technologies

- 🐍 Python 3
- 🔐 cryptography (Fernet)
- 🔑 hashlib (SHA-256 hashing)
- 🧠 base64 (encoding)

---

## 💻 Usage

### ▶️ Install Dependencies

```bash
pip install cryptography
