import joblib
from loguru import logger

from .data_preparation import *

@logger.catch()
def get_predictions(
    filename, sepal_length, sepal_width, petal_length, petal_width
):
    # Load saved standardising object
    scaler = joblib.load("data/scaler.joblib")
    logger.debug("Scaler succesfully loaded.")

    # Load saved classification model
    model = joblib.load(filename)
    logger.debug("Classification model succesfully loaded.")

    X_test = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    # Scaling data
    X_test = scaler.transform(X_test)
    logger.debug("Data succesfully scaled.")
    # Predict class for given data
    y_pred = model.predict(X_test)


    return target_names[y_pred[0]]
