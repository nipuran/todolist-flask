import secrets
from flask_mail import Message
from .extensions import mail
import os


def generate_otp(length=6):
    """Generates a secure OTP of the specified length."""
    otp = secrets.randbelow(10**length - 10**(length-1)) + 10**(length-1)
    return otp

def send_otp_email(email, otp):
    """Sends the OTP to the user's email."""
    msg = Message(
        "Todolist - Your OTP Code",
        sender=os.getenv("EMAIL_SENDER"),
        recipients=[email]
    )
    msg.body = f"Your OTP code is: {otp}. It is valid for the next 5 minutes."
    mail.send(msg)
