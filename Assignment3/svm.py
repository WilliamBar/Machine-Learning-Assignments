from sklearn.datasets import load_svmlight_files
from sklearn import svm
from sklearn.preprocessing import normalize, label_binarize
from sklearn.cross_validation import *
from sklearn.grid_search import GridSearchCV
import pylab as pl

# read training data and validation data merged using cat in satimage.scale.train
X_train, Y_train, X_test, Y_test = load_svmlight_files(["satimage.scale.train","satimage.scale.t"])

# normalize & binarize
X_train = normalize(X_train)
Y_train = label_binarize(Y_train,classes=[1,2,3,4,5,6])[:,5]
X_test = normalize(X_test)
Y_test = label_binarize(Y_test,classes=[1,2,3,4,5,6])[:,5]

# build the classifier

def svm_score(c,d):
    clf = svm.SVC(C=c,kernel='poly',degree=d)
    kfold = KFold(len(Y_train), n_folds=5)
    scores = cross_val_score(clf,X_train,Y_train,cv=kfold,n_jobs=-1)
    return scores.mean()

x = pl.linspace(1,20,20)
y1=[]
y2=[]
y3=[]
for i in x:
    y1.append(svm_score(i,1))
    y2.append(svm_score(i,2))
    y3.append(svm_score(i,3))

pl.plot(x,y1)
pl.hold('on')
pl.plot(x,y2)
pl.plot(x,y3)
pl.legend(['degree = 1','degree = 2', 'degree = 3'])
pl.show()

def svm_test(c):
    clf = svm.SVC(C=c,kernel='poly',degree=1)
    clf.fit(X_train,Y_train)
    return (c,clf.score(X_test,Y_test),clf.n_support_)

xx = pl.linspace(1,20,20)
yy = []

for i in xx:
    yy.append(svm_test(i))
