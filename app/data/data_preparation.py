import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix


data = load_iris()
target_names = {k: v for k, v in enumerate(data.target_names)}

def load_iris_data():
    """Load iris data and assign to the variables. Xs - input data ys - labels"""
    X = data.data
    y = data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,
                                                        random_state=1)
    return X_train, X_test, y_train, y_test


def scale_data(X_train, X_test):
    """Scale the data that they will have std equal 1 to and mean equal to 0."""
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    X_test = sc.transform(X_test)
    return X_train, X_test, sc
