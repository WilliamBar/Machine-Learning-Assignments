import numpy as np
from sklearn.covariance import empirical_covariance

mean = np.random.rand(2)
xx = np.random.rand()
yy = np.random.rand()
xy = np.random.rand()
covariance = [[0.5,0.5],[0.5,0.5]]

covariance[0][0] = xx
covariance[0][1] = xy
covariance[1][0] = xy
covariance[1][1] = yy

print "For non-zero covariance matrix:"
print "===================="

print covariance

for i in xrange(1,8):
    sample_size = 10 ** i
    data = np.random.multivariate_normal(mean,covariance,sample_size)
    predicted_covariance = empirical_covariance(data)
    print predicted_covariance
    mse = ((predicted_covariance - covariance) ** 2).mean()
    print "Sample Size : {1} , Mean Square Error is {0}".format(mse,sample_size)

print "For a diagonal covariance matrix:"
print "===================="

covariance[0][1] = 0
covariance[1][0] = 0
print covariance

for i in xrange(1,8):
    sample_size = 10 ** i
    data = np.random.multivariate_normal(mean,covariance,sample_size)
    predicted_covariance = empirical_covariance(data)
    print predicted_covariance
    mse = ((predicted_covariance - covariance) ** 2).mean()
    print "Sample Size : {1} , Mean Square Error is {0}".format(mse,sample_size)
