import tensorflow as tf

# Load or create your Keras model
# Example: Load model from a .keras file
model = tf.keras.models.load_model('./model/modelC.keras')

# Convert model to JSON format
model_json = model.to_json()

# Save JSON to file
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

print("Model has been converted to JSON and saved to 'model.json'.")
