import configparser
from email.message import EmailMessage
import smtplib

# Load configuration from file
config = configparser.ConfigParser()
config.read('config.ini')

# Retrieve email credentials
EMAIL = config.get('credentials', 'EMAIL')
PASSWORD = config.get('credentials', 'PASSWORD')

def send_email(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL
        email.set_content(message)

        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(EMAIL, PASSWORD)
            smtp.send_message(email)

        print("Email sent successfully")
        return True

    except smtplib.SMTPAuthenticationError:
        print("Authentication Error: Check your email and password.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Example usage
if __name__ == "__main__":
    receiver = "recipient@example.com"
    subject = "Test Email"
    message = "This is a test email sent from the Python script."
    
    send_email(receiver, subject, message)
