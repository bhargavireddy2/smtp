import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
recipients = [
    
    "santhiruler@gmail.com"
    
]
message = """Subject: Test Email
This is a test email sent from a Python script.


"""

server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
server.starttls()
server.login(EMAIL_USER, EMAIL_PASSWORD)

for receiver in recipients:
    server.sendmail(
        EMAIL_USER,
        receiver,
        message
    )
    print(f"Email sent successfully to {receiver}")
server.quit()