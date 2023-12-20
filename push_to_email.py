import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os 
import markdown


def push_to_email(recipient_email, markdown_content):
    # Set your email credentials
    sender_email = os.environ.get("SENDER_EMAIL")
    sender_password = os.environ.get("SENDER_PWD")
    smtp_server = os.environ.get("SMTP_SERVER")
    smtp_port = 587

    # Create the MIME object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Example HTML Email"

    html_content = markdown.markdown(markdown_content)

    # Attach the HTML content to the email
    message.attach(MIMEText(html_content, 'html'))

    # Connect to the SMTP server (in this case, Gmail's SMTP server)
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Start TLS for security
        server.starttls()

        # Login to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())

    print("Email sent successfully!")

if __name__ == "__main__":
    from pathlib import Path
    push_to_email(os.environ.get("TEST_RECIPIENT_EMAIL"), Path("out/output.md").read_text())