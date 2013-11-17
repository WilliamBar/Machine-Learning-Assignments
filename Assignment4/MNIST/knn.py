from numpy import *
from sklearn import cross_validation
from sklearn import neighbors, datasets
from sklearn.datasets import fetch_mldata

# Loading data
mnist = fetch_mldata("MNIST original")
X, Y = mnist.data, mnist.target

n_neighbors = 3

# Rescale grayscale from -1 to 1
X = X/255.0*2 - 1

# Shuffle the input
shuffle = random.permutation(arange(X.shape[0]))
X, Y = X[shuffle], Y[shuffle]

#X = X[:5000]
#Y = Y[:5000]
clf = neighbors.KNeighborsClassifier(n_neighbors,weights="distance",algorithm="ball_tree")

# Train and validate the model with 10-fold cross validation
scores = cross_validation.cross_val_score(clf, X, Y, cv=10, n_jobs=1)

print scores
print mean(scores)
