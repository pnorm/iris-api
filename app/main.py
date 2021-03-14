import uvicorn
import joblib
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from loguru import logger

from data.predictions_handler import *


class ModelName(str, Enum):
    decision_tree = "Decision Tree"
    naive_bayes = "Gaussian Naive Bayes"
    nearest_centroid = "Nearest Centroid"


# Initiate logging
log_format = "{time} | {level} | {message} | {file} | {line} | {function} | {exception}"
logger.add(sink='data/log_files/logs.log', format=log_format, level='DEBUG', compression='zip')


app = FastAPI(title="What type of iris is it?", version="1.0",
              description="Setosa, versicolor or virginica?")


@app.get("/predict")
@logger.catch()
async def get_prediction(
    model_name: ModelName, sepal_length: float, sepal_width: float,
    petal_length: float, petal_width: float
):
    logger.info("User sent some data for prediction.")

    if model_name == ModelName.decision_tree:
        predicted_class = get_predictions(
            "data/model_decisiontreeclassifier.joblib", sepal_length, sepal_width,
            petal_length, petal_width
        )
    elif model_name == ModelName.naive_bayes:
        predicted_class = get_predictions(
            "data/model_gaussiannb.joblib", sepal_length, sepal_width,
            petal_length, petal_width
        )
    else:
        predicted_class = get_predictions(
            "data/model_nearestcentroid.joblib", sepal_length, sepal_width,
            petal_length, petal_width
        )
    logger.debug("Prediction succesfully generated for the user.")
    return {"model_name": model_name, "predicted_class": predicted_class}


# if __name__=="__main__":
#     uvicorn.run(app, port=8000, host="0.0.0.0")
