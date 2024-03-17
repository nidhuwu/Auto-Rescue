from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = load_model('car_accident_classifier.h5')

# Path to the test image
test_image_path = r'img_dataset\test\accident\test1_27.jpg'
# test_image_path = r'C:\Users\hp\Desktop\download.jpg'
# test_image_path = r'C:\Users\hp\Desktop\images.jpg'
# Function to make predictions on a single image
def predict_single_image(img_path):
    img = image.load_img(img_path, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale pixel values to between 0 and 1

    prediction = model.predict(img_array)

    # Print the raw prediction value
    print("Raw Prediction Value:", prediction[0][0])

    if prediction[0][0] > 0.7:
        return "Car Accident"
    else:
        return "No Car Accident"


# Test the model on the specified image
prediction = predict_single_image(test_image_path)
print(f"Prediction for {test_image_path}: {prediction}")
