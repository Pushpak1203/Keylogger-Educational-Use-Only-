# 🧠 Keylogger (Educational Use Only)

This project is a simple educational keylogger built with Python. It captures keyboard inputs, optionally encrypts them, and can send them to your email securely. Designed for ethical and controlled environments only (e.g., cybersecurity learning labs).

> ⚠️ **WARNING:** This software is for educational purposes ONLY. Unauthorized use may be illegal and unethical.

---

## 📁 Project Structure

```
keylogger-educational/
│
├── app.py                  # Entry point
├── config.py               # Configurations (log path, email, etc.)
├── requirements.txt        # Python dependencies
├── logs/                   # Stores keystroke logs
│   └── keylog.txt
│
├── logger/
│   ├── __init__.py
│   ├── keylogger.py        # Core logic to capture keys
│   └── encryptor.py        # Optional: Encrypt logs with Fernet
│
├── utils/
│   └── mailer.py           # Send logs via email
└── README.md
```

---

## ✅ Features

- 🔑 Captures keystrokes using `pynput`
- 🔐 Optional AES-like symmetric encryption using `cryptography`
- 📧 Emails logs securely with SMTP + SSL
- 🛡️ Designed with ethical, educational use in mind

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Pushpak1203/keylogger-educational.git
cd keylogger-educational
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# OR
source venv/bin/activate   # On Linux/macOS
```

### 3. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Configure `config.py`
Set email credentials, log paths, encryption preference, etc.

### 5. Run the Keylogger
```bash
python app.py
```

> Press `ESC` to stop logging.

---

## 🔐 Gmail App Password Note

If you're using Gmail to send logs:
1. Enable 2FA in your Google account.
2. Generate an **App Password** from https://myaccount.google.com/apppasswords
3. Use that password in `config.py` as `EMAIL_PASSWORD`.

---

## 📜 License

MIT License – Use responsibly.

---

## ✍️ Author

Pushpak Chakraborty