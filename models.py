import tensorflow as tf

#? -----------------------------------------------------------------------------
#? Cancino's Config 
#? -----------------------------------------------------------------------------

epochs_cancino = 8

model_cancino = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(784,)),
    tf.keras.layers.Dense(units = 400, activation="relu"),
    tf.keras.layers.Dropout(0.3),
    tf.keras.layers.Dense(units = 250, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units = 200, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(units = 100, activation="relu"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(units = 100, activation="relu"),
    tf.keras.layers.Dense(units = 47, activation="softmax"),
])

#! -----------------------------------------------------------------------------
#! JP's Config 
#! -----------------------------------------------------------------------------

epochs_jp = 10
# V1 loss .5049 accuracy .8349
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

# V2 loss .4961 accuracy .8383
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

# V3 loss .4903 accuracy .8423
# model_jp = tf.keras.Sequential([
#     tf.keras.layers.Input(shape=(784,)),
#     tf.keras.layers.Dense(units = 512, activation="relu"),
#     tf.keras.layers.Dropout(0.2),
#     tf.keras.layers.Dense(units = 256, activation="relu"),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Dense(units = 512, activation="relu"),
#     tf.keras.layers.Dropout(0.25),
#     tf.keras.layers.Dense(units = 128, activation="relu"),
#     tf.keras.layers.Dropout(0.1),
#     tf.keras.layers.Dense(units = 32, activation="relu"),
#     tf.keras.layers.Dense(units = 47, activation="softmax"),
# ])