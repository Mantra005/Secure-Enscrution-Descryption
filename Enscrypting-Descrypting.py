import base64
import getpass
import os
from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def make_fernet(password: str, salt: bytes) -> Fernet:
    """Derive an encryption key from the password and per-message salt."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=600_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode("utf-8")))
    return Fernet(key)


while True:
    action = input("Encrypt or decrypt? [e/d, 0/exit to quit]: ").strip().lower()

    if action in {"0", "exit"}:
        break
    elif action == "e":
        message = input("Enter message to encrypt: ")
        password = getpass.getpass("Password: ")
        salt = os.urandom(16)
        token = make_fernet(password, salt).encrypt(message.encode("utf-8"))
        # Include the random salt so the same password can decrypt this message.
        encoded = base64.urlsafe_b64encode(salt + token).decode("ascii")
        print(encoded.rstrip("="))
    elif action == "d":
        encoded = input("Enter encrypted message: ").strip()
        password = getpass.getpass("Password: ")
        try:
            # Padding is optional in the displayed form; restore it before decoding.
            encoded += "=" * (-len(encoded) % 4)
            payload = base64.urlsafe_b64decode(encoded.encode("ascii"))
            salt, token = payload[:16], payload[16:]
            message = make_fernet(password, salt).decrypt(token).decode("utf-8")
            print(message)
        except (ValueError, UnicodeError, InvalidToken):
            print("Decryption failed: invalid message or password.")
    else:
        print("Choose 'e' to encrypt, 'd' to decrypt, or '0'/'exit' to quit.")


