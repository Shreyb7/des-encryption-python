# 🔐 DES Encryption in Python

A simple Python implementation demonstrating **DES (Data Encryption Standard)** encryption and decryption using the **PyCryptodome** library.

---

## 📖 Overview

The Data Encryption Standard (DES) is one of the earliest symmetric-key encryption algorithms. Although it has been superseded by more secure algorithms such as AES, DES remains an important algorithm for understanding the fundamentals of cryptography.

This project demonstrates how plaintext can be encrypted and decrypted using DES in Python.

> **Note:** This implementation is intended for educational purposes only. DES is considered insecure for modern applications due to its small key size.

---

## ✨ Features

- DES Encryption
- DES Decryption
- Interactive user input
- Beginner-friendly implementation
- Command-line interface

---

## 🛠 Technologies Used

- Python 3
- PyCryptodome

---

## 📦 Installation

Install PyCryptodome:

```bash
pip install pycryptodome
```

---

## 🚀 Running the Program

Clone the repository:

```bash
git clone https://github.com/Shreyb7/des-encryption-python.git
```

Navigate into the folder:

```bash
cd des-encryption-python
```

Run:

```bash
python des_encryption_demo.py
```

---

## 📂 Repository Structure

```
des-encryption-python
│
├── des_encryption_demo.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📚 Learning Objectives

- Understand symmetric key cryptography
- Learn DES encryption
- Learn DES decryption
- Understand block cipher concepts
- Explore Python cryptography libraries

---

## 📌 Example

```
Enter plaintext:
Hello World

Encrypted Ciphertext:
b'...'

Decrypted Plaintext:
Hello World
```

---


DES is considered cryptographically insecure because of its 56-bit key size. Modern applications should use AES instead.
