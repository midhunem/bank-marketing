from fastapi import FastAPI
from src.utils import preprocess_input
from src.logger import get_logger
from src.ml_model import predict_adaboost
import ast
import pandas as pd
import pickle
app = FastAPI()
logger = get_logger(__name__)

@app.post("/predict/")
async def predict(data):
    logger.info("Received prediction request.")
    try:
        data = ast.literal_eval(data)
        processed_data = preprocess_input(data)
        prediction = predict_adaboost(processed_data)
        logger.info("Prediction successful.")
        return {"prediction": str(prediction)}
    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        return {"error": "Prediction failed"}

