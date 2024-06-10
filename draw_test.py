import numpy as np
import tensorflow as tf
from flask import Flask, request, jsonify, render_template
import re
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Load the model
model_path = './model/modelC.keras'
model = tf.keras.models.load_model(model_path)

# Function to prepare the image
def prepare_image(img, target_size=(150, 150)):
    if img.mode != "RGB":
        img = img.convert("RGB")
    img = img.resize(target_size)
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

@app.route('/')
def home():
    return render_template('draw.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    img_str = re.search(r'base64,(.*)', data['image']).group(1)
    img_data = base64.b64decode(img_str)
    img = Image.open(BytesIO(img_data))

    img_array = prepare_image(img)

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=1)
    confidence_score = np.max(predictions, axis=1)[0]

    # Class names should be consistent with your model's output
    class_names = ['ba', 'ca', 'da', 'dha', 'ga', 'ha', 'ja', 'ka', 'la', 'ma', 'na', 'nga', 'nya', 'pa', 'ra', 'sa', 'ta', 'tha', 'wa', 'ya']
    predicted_class_name = class_names[predicted_class_index[0]]

    return jsonify(prediction=predicted_class_name, confidence=confidence_score * 100)

if __name__ == '__main__':
    app.run(debug=True)
