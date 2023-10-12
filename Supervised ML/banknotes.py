import csv
import tensorflow as tf
from sklearn.model_selection import train_test_split
import pandas as pd

data = pd.read_csv('C:\\Users\\Siddh\\Desktop\\banknotes.csv')

evidence = data.iloc[:, 0:4]
labels = data.iloc[:, -1]

X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size = 0.4
)

# Create a neural network
model = tf.keras.models.Sequential()

# Add a hidden layer with 8 units, with ReLU activation
model.add(tf.keras.layers.Dense(8, input_shape=(4,), activation="relu"))

# Add output layer with 1 unit, with sigmoid activation
model.add(tf.keras.layers.Dense(1, activation="sigmoid"))

# Train neural network
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
model.fit(X_training, y_training, epochs=20)

# Evaluate how well model performs
model.evaluate(X_testing, y_testing, verbose=2)
