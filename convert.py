import os
import tensorflow as tf

# Menonaktifkan oneDNN custom operations
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# Memuat model Keras dari file
model = tf.keras.models.load_model('./model/modelC.keras')

# Mengonversi arsitektur model ke format JSON
model_json = model.to_json()

# Menyimpan arsitektur model ke file JSON
with open('model.json', 'w') as json_file:
    json_file.write(model_json)

print("Model architecture has been saved to 'model.json'.")

# Menyimpan bobot model ke file HDF5 dengan ekstensi .bin
model.save_weights('model_weights.h5')

# Mengganti nama file HDF5 menjadi .bin
os.rename('model_weights.h5', 'model_weights.bin')

print("Model weights have been saved to 'model_weights.bin'.")
