from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.naive_bayes import GaussianNB

from data_preparation import *

classifiers = [DecisionTreeClassifier(), GaussianNB(), NearestCentroid()]

def predict_target_class(
    classifier, sepal_length, sepal_width, petal_length, petal_width
):
    # Load and scale load iris data
    X_train, X_test, y_train, y_test = load_iris_data()
    X_train, X_test, sc = scale_data(X_train, X_test)

    # Make classifier instance
    clf = classifier

    # Train model
    model = clf.fit(X_train, y_train)

    score = clf.score(X_test, y_test)
    print(f"Score on the test data: {round(score, 4)}")

    # Predict data
    y_pred = model.predict(X_test)

    # Print confusion matrix to see how good the model perform on the test data
    print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")

    # Predict
    X_test = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    y_pred = model.predict(X_test)

    return target_names[y_pred[0]], sc


for classifier in classifiers:
    y_pred, clf = predict_target_class(classifier, 0.5, 0.1, 0.6, 0.2)
    classifier_name = str(classifier).replace("()", "")
    print(f"{classifier_name}: {y_pred}")
