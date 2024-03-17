import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import sqlite3
from math import radians, sin, cos, sqrt, atan2

def haversine(lat1, lon1, lat2, lon2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # Calculate the differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    # Calculate the distance
    distance = R * c

    return distance

def get_nearest_user(accident_lat, accident_lon):
    # Connect to SQLite database
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()

    # Query all data from the users table
    cursor.execute('SELECT * FROM users')
    users_data = cursor.fetchall()

    # Close connection
    conn.close()

    nearest_user = None
    min_distance = float('inf')

    for user in users_data:
        user_id = user[0]
        user_name = user[1]

        # Convert latitude and longitude to float
        user_lat = float(user[4])  # assuming latitude is in the 5th column
        user_lon = float(user[5])  # assuming longitude is in the 6th column

        distance = haversine(accident_lat, accident_lon, user_lat, user_lon)

        if distance < min_distance:
            min_distance = distance
            nearest_user = {'id': user_id, 'name': user_name, 'distance': distance}

    return nearest_user

def send_email_with_attachment(image_path, receiver_email):
    # Set up the email server
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587

    # Sender email address
    sender_email = 'iknaragude101@gmail.com'
    password = 'ybhe nfrp fwgu lime'  # Use your actual Gmail password

    # Create the email message
    subject = 'Car Accident Alert'
    body = 'Car accident detected. Please check the attached image for details.'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the body of the email
    message.attach(MIMEText(body, 'plain'))

    # Attach the image file
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

def predict_and_send_email(img_path):
    # Load the trained model
    model = load_model('car_accident_classifier.h5')

    # Function to make predictions on a single image
    def predict_single_image(img_path):
        img = image.load_img(img_path, target_size=(64, 64))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0  # Rescale pixel values to between 0 and 1

        prediction = model.predict(img_array)

        # Print the raw prediction value
        print("Raw Prediction Value:", prediction[0][0])

        return prediction[0][0]

    # Test the model on the specified image
    prediction_value = predict_single_image(img_path)

    if prediction_value > 0.65:
        print(f"Prediction for {img_path}: Car Accident detected.")

        # Get the accident location coordinates (replace with actual values)
        accident_latitude = 72.101
        accident_longitude = 71.508

        # Get the nearest user
        nearest_user = get_nearest_user(accident_latitude, accident_longitude)

        if nearest_user:
            receiver_email = 'indrakumarhn01@gmail.com'  # Replace with the email of the nearest user
            send_email_with_attachment(img_path, receiver_email)
        else:
            print("No registered users found.")
    else:
        print(f"Prediction for {img_path}: No Car Accident detected.")

# Path to the test image
test_image_path = r'vav\test\non_accident\test7_39.jpg'
# Call the function to predict and send email if necessary
predict_and_send_email(test_image_path)
