import pandas as pd # data loading and manipulation
import matplotlib.pyplot as plt # plotting
import seaborn as sns # statistical plotting

from sklearn.model_selection import train_test_split 
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = svm.SVC() ### best option for this dataset
# model = Perceptron()
# model = svm.SVC()
# model = KNeighborsClassifier(n_neighbors=1)
# model = GaussianNB()

diabetes = pd.read_csv("diabetes.csv")

print(diabetes.head())
print(diabetes.info())
print(diabetes.shape)
print(diabetes.describe())
print(diabetes.corr())

features = diabetes.iloc[:, 0:8]
labels = diabetes.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size = 0.20, random_state = 42 # seed for shuffling
) 

# fit the model off the training set
model = model.fit(X_train, y_train)

# make predictions on the testing set
predictions = model.predict(X_test)

# compute the performance
correct = (predictions == y_test).sum()
incorrect = (predictions != y_test).sum()
total = correct + incorrect

# Print results
print(f"Results for model {type(model).__name__}")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Accuracy: {100 * correct / total:.2f}%")