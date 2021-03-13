from sklearn.naive_bayes import GaussianNB

from data_preparation import *


# Load and scale load iris data
X_train, X_test, y_train, y_test = load_iris_data()
X_train, X_test, sc = scale_data(X_train, X_test)

# Gaussian Naive Bayes classifier instance
clf = GaussianNB()

# Train mode
model = clf.fit(X_train, y_train)

score = clf.score(X_test, y_test)
print(f"Score on the test data: {round(score, 4)}")

# Predict data
y_pred = model.predict(X_test)

# Print confusion matrix to see how good the model perform on the test data
print(f"Confusion matrix:\n{confusion_matrix(y_test, y_pred)}")

# Predict
def predict_target_class(sepal_length, sepal_width, petal_length, petal_width):
    X_test = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    y_pred = model.predict(X_test)
    return target_names[y_pred[0]]

print(predict_target_class(0.5, 0.1, 0.6, 0.2))
