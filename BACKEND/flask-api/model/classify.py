from flask import Flask, request, jsonify
import tensorflow as tf
from PIL import Image
import numpy as np

app = Flask(__name__)

# Load pre-trained ML model (adjust path to your model)
model = tf.keras.models.load_model(r'C:\Users\dhruv\OneDrive\Desktop\website_rail\project-root\flask-api\washroom_classification_model.h5')

def preprocess_image(image_path):
    img = Image.open(image_path).resize((224, 224))
    img = np.array(img) / 255.0  # Normalize pixel values
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

@app.route('/classify', methods=['POST'])
def classify_washroom():
    data = request.get_json()
    file_path = data['filePath']

    # Preprocess the image for the ML model
    image = preprocess_image(file_path)
    prediction = model.predict(image)

    # Assuming the model output is a probability: 0 -> dirty, 1 -> clean
    result = 'clean' if prediction[0][0] > 0.5 else 'dirty'
    
    return jsonify({'classification': result})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
