import csv
import random

from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd


model = KNeighborsClassifier(n_neighbors = 2)
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()

data = pd.read_csv('C:\\Users\\Siddh\\Desktop\\banknotes\\banknotes.csv')

evidence = data.iloc[:, 0:4]
labels = data.iloc[:, -1]

X_training, X_testing, y_training, y_testing = train_test_split(
    evidence, labels, test_size = 0.4
)

model.fit(X_training, y_training)

# make predicts on the testing set
predictions = model.predict(X_testing)

print(X_training)

# Compute how well we performed
correct = (y_testing == predictions).sum()
incorrect = (y_testing != predictions).sum()
total = len(predictions)

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")