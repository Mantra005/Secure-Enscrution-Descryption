# Secure-Enscrution-Descryption
A secure, portable CLI tool written in Python to encrypt and decrypt text messages using password-based AES encryption. Share the generated token and password with anyone to let them decrypt the message on their own machine.

# Portable Password-Based Text Encrypter

A zero-dependency footprint, highly secure Python CLI utility to encrypt and decrypt text messages using a password. Because the script embeds a unique cryptographic salt straight into the encrypted payload, **the generated text is completely portable**. You can safely share the encrypted text string and the password with a friend, and they will be able to decrypt it on their own machine.

## 🔒 Security Features
* **Fernet Symmetric Encryption:** Built on AES-128 in CBC mode with an HMAC-SHA256 signature to guarantee the data cannot be read or tampered with.
* **Hardened Key Derivation:** Uses `PBKDF2HMAC` with a SHA-256 backend running **600,000 iterations** to convert your plaintext password into a strong cryptographic key, rendering brute-force attacks computationally unfeasible.
* **Unique Salting:** A unique 16-byte random salt (`os.urandom`) is generated on every single encryption operation. Even if you encrypt the same phrase twice with the same password, the outputs will look completely different.

## 🛠️ Prerequisites
* Python 3.8 or higher.
* The `cryptography` Python library.

## 🚀 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd YOUR_REPO_NAME
   ```

2. **Set up a virtual environment (Recommended):**
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 How to Use

Run the main script from your terminal:
```bash
python main.py
```

### 1. Encrypting a Message
1. Input `e` when prompted.
2. Type out the message you wish to obscure.
3. Provide a password (your keystrokes will be securely hidden by the console terminal).
4. Copy the generated base64 text string.

### 2. Decrypting a Message
1. Input `d` when prompted.
2. Paste the encrypted text string string.
3. Provide the correct matching password.
4. The system will cleanly output the decrypted plain text.

### 3. Exiting the Tool
* Input `0` or `exit` at the primary prompt to terminate the interactive loop cleanly.

