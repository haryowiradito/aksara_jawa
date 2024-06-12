import tensorflow as tf

# Muat model SavedModel
new_model = tf.keras.models.load_model('./model/modelC.keras')

# Periksa arsitektur model
new_model.summary()

# Simpan model dalam format .h5
new_model.save('model.h5')
