import joblib

from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB

from .data_preparation import *

classifiers = [DecisionTreeClassifier(), GaussianNB(), NearestCentroid()]

# Load and scale load iris data
X_train, X_test, y_train, y_test = load_iris_data()
X_train, X_test, sc = scale_data(X_train, X_test)

def create_model(classifier, X_train, y_train):
    classifier_name = str(classifier).replace("()", "")
    model = classifier.fit(X_train, y_train)
    return model, classifier_name

for classifier in classifiers:
    model, classifier_name = create_model(classifier, X_train, y_train)
    # Save model objects
    joblib.dump(model, "model_" + classifier_name.lower() + ".joblib")

joblib.dump(sc, "scaler.joblib")
