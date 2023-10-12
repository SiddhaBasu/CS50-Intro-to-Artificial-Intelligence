import random
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

model = KNeighborsClassifier(n_neighbors=3)
# model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()

df= pd.read_csv('kerala.csv')
print(df.head())
print(df.info())
print(df.shape)
print(df.describe())
print(df.corr())

df['FLOODS'].replace(['YES', 'NO'], [1, 0], inplace=True)

evidence = df.iloc[:, 1:14]
label = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    evidence, label, test_size = 0.4, random_state = 1001
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

# Compute how well we performed
correct = (y_test == predictions).sum()
incorrect = (y_test != predictions).sum()
total = len(predictions)

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")