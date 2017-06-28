#use svm for breast cancer ML
from sklearn.svm import SVC
from time import time
import numpy as np


#read data
features_train=np.loadtxt("data_train.txt")
labels_train=np.loadtxt("labels_train.txt")
features_test=np.loadtxt("data_test.txt")
labels_test=np.loadtxt("labels_test.txt")

#hv = HashingVectorizer()
#vectorizer = CountVectorizer(min_df=1)

#features_train=preprocessor(data_train)
#labels_train=labelstrain.read()
#features_test=data_test.read()
#labels_test=labelstest.read()

#make data sklearn-friendly

print len(features_train),len(labels_train),len(features_test),len(labels_test)




def svmClassify(features_train,labels_train):
	clf=SVC(C=10000,kernel="rbf",gamma=0.000001)
	t0 = time()
	clf.fit(features_train,labels_train)
	print "training time:", round(time()-t0, 3), "s"

	return clf

t0=time()
clf=svmClassify(features_train,labels_train)
pred= clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"



#accuracy
accuracy = clf.score(features_test,labels_test)
print "Accuracy is", accuracy

#Their accuracy
