import tensorflow as tf

# Load or create your Keras model
model = tf.keras.models.load_model('./model/modelC.keras')

# Convert model architecture to JSON format
model_json = model.to_json()

# Save JSON to file
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

print("Model architecture has been saved to 'model.json'.")

# Save model weights to a binary file
model.save_weights('model_weights.bin')

print("Model weights have been saved to 'model_weights.bin'.")
