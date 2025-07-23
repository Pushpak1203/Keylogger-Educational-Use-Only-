"""
Keylogger Package Initialization

This package contains modules related to:
- Capturing keystrokes using pynput (keylogger.py)
- Encrypting logs if needed (encryptor.py)
"""

from .keylogger import KeyLogger

# Optional: If encryptor.py has classes/functions you want to expose
try:
    from .encryptor import encrypt_log
except ImportError:
    encrypt_log = None  # Encryption is optional

__all__ = ["KeyLogger", "encrypt_log"]
