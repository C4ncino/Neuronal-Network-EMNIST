import tensorflow as tf

path = 'models/cancino/v4'

player = 'cancino'

#? -----------------------------------------------------------------------------
#? Cancino's Config 
#? -----------------------------------------------------------------------------

epochs_cancino = 15

model_cancino = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(180, activation='relu'),
    tf.keras.layers.Dropout(0.15),
    tf.keras.layers.Dense(180, activation='relu'),
    tf.keras.layers.Dropout(0.15),
    tf.keras.layers.Dense(units = 47, activation="softmax"),
])

#! -----------------------------------------------------------------------------
#! JP's Config 
#! -----------------------------------------------------------------------------

epochs_jp = 5

model_jp = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(units = 256, activation="relu"),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(units = 256, activation="relu"),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(units = 128, activation="relu"),
    tf.keras.layers.Dropout(0.12),
    tf.keras.layers.Dense(units = 128, activation="relu"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(units = 64, activation="relu"),
    tf.keras.layers.Dense(units = 47, activation="softmax"),
])