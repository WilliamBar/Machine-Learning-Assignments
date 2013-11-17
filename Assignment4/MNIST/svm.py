from numpy import *
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.datasets import fetch_mldata

# Loading data
mnist = fetch_mldata("MNIST original")
X, Y = mnist.data, mnist.target

# Rescale grayscale from -1 to 1
X = X/255.0*2 - 1

# Shuffle the input
shuffle = random.permutation(arange(X.shape[0]))
X, Y = X[shuffle], Y[shuffle]

# Initialise the model, the best model parameters are reported at
# http://peekaboo-vision.blogspot.co.uk/2010/09/mnist-for-ever.html
clf = SVC(kernel="rbf", C=2.8, gamma=.0073)

# Train and validate the model with 10-fold cross validation
scores = cross_validation.cross_val_score(clf, X, Y, cv=10, n_jobs=1)

print scores
