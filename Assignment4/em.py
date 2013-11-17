import numpy as np
from pypr.clustering import *
from sklearn import mixture

means = [np.random.rand(2) for _ in xrange(3)]
ccov = []
for i in xrange(3):
    xx = np.random.rand()
    yy = np.random.rand()
    xy = np.random.rand()
    covariance = [[0.5,0.5],[0.5,0.5]]

    covariance[0][0] = xx
    covariance[0][1] = xy
    covariance[1][0] = xy
    covariance[1][1] = yy
    ccov.append(covariance)


weights1 = [0.2,0.3,0.5]
weights2 = [0.7,0.2,0.1]
print "Actual Weights : (0.2,0.3,0.5) "


for i in xrange(1,6):
    sample_size = 10**i
    data = gmm.sample_gaussian_mixture(means,ccov,weights1,sample_size)
    g = mixture.GMM(n_components=3)
    g.fit(data)
    print "Sample Size : {0} , Predicted Weights {1}".format(sample_size,np.round(g.weights_,2))
    # print g.weights_
    # print g.means_
    # print g.covars_

print "Actual Weights : (0.7,0.2,0.1) "


for i in xrange(1,6):
    sample_size = 10**i
    data = gmm.sample_gaussian_mixture(means,ccov,weights2,sample_size)
    g = mixture.GMM(n_components=3)
    g.fit(data)
    print "Sample Size : {0} , Predicted Weights {1}".format(sample_size,np.round(g.weights_,2))
    # print g.weights_
    # print g.means_
    # print g.covars_
