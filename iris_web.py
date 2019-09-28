from sklearn import datasets
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from sklearn import tree
import sys

def initialize_clf():
	# create features and labels
	iris = datasets.load_iris()
	features = iris.data
	labels = iris.target

	# make decision tree classifier
	clf = tree.DecisionTreeClassifier()

	# train the classifier
	clf.fit(features, labels)

	return clf

def predict(clf, inputs):
	prediction = clf.predict([inputs])
	return prediction