from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np
import cv2

app = Flask(__name__)

# Load pre-trained ML model
model = tf.keras.models.load_model(r'C:\Users\dhruv\OneDrive\Desktop\website_rail\project-root\flask-api\washroom_classification_model.h5')

def preprocess_image(image_path):
    # Preprocess image for the ML model
    img = Image.open(image_path).resize((224, 224)) # Resize image as per your model's input size
    img = np.array(img) / 255.0  # Normalize pixel values to [0,1]
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/classify', methods=['POST'])
def classify_washroom():
    data = request.get_json()
    file_path = data['filePath']

    # Preprocess the image for the ML model
    image = preprocess_image(file_path)
    prediction = model.predict(image)

    # Assuming the model outputs a probability: 0 -> dirty, 1 -> clean
    result = 'clean' if prediction[0][0] > 0.5 else 'dirty'
    
    return jsonify({'classification': result})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
