# logger/encryptor.py

from cryptography.fernet import Fernet
import os

# Default path to store/retrieve encryption key
KEY_FILE = "secret.key"

def generate_key(path: str = KEY_FILE) -> bytes:
    """
    Generate and save a new symmetric encryption key.
    """
    key = Fernet.generate_key()
    with open(path, 'wb') as key_file:
        key_file.write(key)
    return key

def load_key(path: str = KEY_FILE) -> bytes:
    """
    Load the previously generated encryption key.
    """
    if not os.path.exists(path):
        return generate_key(path)
    with open(path, 'rb') as key_file:
        return key_file.read()

def encrypt_log(log_data: str, key: bytes = None) -> bytes:
    """
    Encrypt the given log data (plaintext string) using Fernet.
    """
    if key is None:
        key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(log_data.encode())

def decrypt_log(encrypted_data: bytes, key: bytes = None) -> str:
    """
    Decrypt encrypted log data back to plaintext.
    """
    if key is None:
        key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_data).decode()
