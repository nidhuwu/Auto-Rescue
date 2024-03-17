import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders


def send_email_with_attachment():
    # Set up the email server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

   # Sender and receiver email addresses
    sender_email = 'iknaragude101@gmail.com'
    receiver_email = 'indrakumarhn01@gmail.com'
    password = 'ybhe nfrp fwgu lime'  # Use your actual Gmail password

    # Create the email message
    subject = 'World cup India'
    body = 'Winner Team india, Congratulations on winning 3rd championship'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach an image file (replace 'path/to/your/image.jpg' with the actual path)
    image_path = 'C:/Users/hp/Pictures/Saved Pictures/India.jpg'
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    image_attachment = MIMEImage(image_data, name='image.jpg')
    message.attach(image_attachment)

    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print('Mail with image sent successfully!')
    except smtplib.SMTPAuthenticationError as e:
        print(f"SMTP Authentication Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


# Call the function to send the email with the image
send_email_with_attachment()
