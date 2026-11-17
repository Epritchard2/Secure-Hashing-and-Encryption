This is a simple Python program for my introductory cybersecurity class. It demonstrates hashing, encryption, and digital signatures.

## Features

- **SHA-256:** Creates a hash of text or a file.
- **Caesar cipher:** Encrypts and decrypts text by shifting letters. Spaces, punctuation, and capitalization are preserved.
- **RSA signatures:** Signs a message, verifies it, and shows that changing the message makes verification fail. The cryptography library handles RSA, and keys are not saved.

The Caesar cipher is for learning only and is not secure for real use.

## How to Run

Install Python 3 and open this folder in VS Code. In **Terminal > New Terminal**, run:

powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe security_demo.py


After setup, only the last command is needed.

## How It Works

Choose a menu option and follow the prompts. For the cipher, enter a message and a whole-number shift. Use the same shift to decrypt. Choose 5 to exit.

## Testing

Text and file hashes matched hashlib. With shift 3, Hello, Zz! became Khoor, Cc! and decrypted correctly. The original signed message passed verification; the changed message failed.

## What I Learned

Hashing creates a fingerprint that cannot be decrypted. Encryption can be reversed with the right key. Digital signatures check that a message matches what was signed, but do not hide it.
