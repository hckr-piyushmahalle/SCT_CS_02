# 🖼️ Image Encryption Tool – Caesar Cipher Alternative  
**Cyber Security Internship - SkillCraft Technology**  
**Task 02 | Track Code: CS**

---

## 🔐 Overview

This is a simple image encryption and decryption tool built using Python.  
It uses a password-based XOR algorithm to encrypt any image file (e.g., `.jpg`, `.png`), and then decrypts it using the same password.

The tool is terminal-based and provides a clean, menu-driven interface for user interaction.

---

## ⚙️ Features

- 🔑 **Password-based encryption** (string key instead of single number)
- ✅ Detects incorrect passwords using a built-in signature check
- 📂 Works with most image formats like `.jpg`, `.jpeg`, `.png`
- 🧠 Reversible encryption (XOR logic)
- 🖥️ Terminal-based menu system
- 📊 Progress display during encryption/decryption

---

## 🛠️ How It Works

1. User selects an image to encrypt
2. Enters a password (used as encryption key)
3. Tool XORs the file content using the password and adds a signature
4. Decryption with the same password restores the original image
5. Wrong passwords are rejected with an error message

---

## 🚀 Technologies Used

- Python 3
- File handling and byte operations
- XOR-based encryption logic
- Console I/O

---

## 🧪 Sample Output

=== Image Encryption Tool ===

Encrypt an image

Decrypt an image

Exit

Enter image file name (in this folder): sample.jpg
Enter password: mysecret123
Progress: 90%
✅ Done! Output saved as: sample_enc.jpg



---

## 📌 Note

- Use the same password for encryption and decryption
- Output files will be named:
  - `original_enc.jpg` (encrypted)
  - `original_dec.jpg` (decrypted)
- Do not rename the encrypted files before decrypting

---

## ✅ Status

Task 02 Completed ✔  
Submitted as part of the Cyber Security Internship at **SkillCraft Technology**.

