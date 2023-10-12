# K-Means Clustering
    # iterative approach which initializes random cluster centroid placement
    # the clusters are assigned based off of which centroid is the closest to those data points
    # the centroids are moved to the center of its cluster points
    # this process is repeated until there is an equilibrium
    # k represents number of clusters

from sklearn import datasets
from sklearn.cluster import KMeans

# Loading dataset
iris_df = datasets.load_iris()

# Declaring Model
model = KMeans(n_clusters=3)

# Fitting Model
model.fit(iris_df.data)

# Predicitng a single input
predicted_label = model.predict([[7.2, 3.5, 0.8, 1.6]])

# Prediction on the entire data
all_predictions = model.predict(iris_df.data)

# Printing Predictions
print(predicted_label)
print(all_predictions)