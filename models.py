import tensorflow as tf

path = 'models/cancino/v5'

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

epochs_jp = 10
# V1 loss .4883 accuracy .8445
# model_jp = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(784,)),
#     tf.keras.layers.Dense(units = 512, activation="relu"),
#     tf.keras.layers.Dropout(0.20),
#     tf.keras.layers.Dense(units = 256, activation="relu"),
#     tf.keras.layers.Dropout(0.20),
#     tf.keras.layers.Dense(units = 128, activation="relu"),
#     tf.keras.layers.Dropout(0.10),
#     tf.keras.layers.Dense(units = 256, activation="relu"),
#     tf.keras.layers.Dropout(0.1),
#     tf.keras.layers.Dense(units = 64, activation="relu"),
#     tf.keras.layers.Dense(units = 47, activation="softmax"),
# ])

# V2 loss .4984 accuracy .8353
# model_jp = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(784,)),
#     tf.keras.layers.Dense(units = 512, activation="relu"),
#     tf.keras.layers.Dropout(0.20),
#     tf.keras.layers.Dense(units = 256, activation="relu"),
#     tf.keras.layers.Dropout(0.20),
#     tf.keras.layers.Dense(units = 512, activation="relu"),
#     tf.keras.layers.Dropout(0.20),
#     tf.keras.layers.Dense(units = 64, activation="relu"),
#     tf.keras.layers.Dropout(0.1),
#     tf.keras.layers.Dense(units = 32, activation="relu"),
#     tf.keras.layers.Dense(units = 47, activation="softmax"),
# ])

# V3 loss .4896 accuracy .8393
model_jp = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(units = 512, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units = 256, activation="relu"),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(units = 512, activation="relu"),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Dense(units = 128, activation="relu"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(units = 32, activation="relu"),
    tf.keras.layers.Dense(units = 47, activation="softmax"),
])