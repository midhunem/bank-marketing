import pickle
import numpy as np

def predict_adaboost(data):
    """
    Predicts using a trained AdaBoost model.

    Parameters:
    - data : Input data for prediction.

    Returns:
    - y_pred : Predicted labels.
    """
    with open('models/model.pkl', 'rb') as f:
        model = pickle.load(f)
    y_pred = model.predict(np.array(data))
    return y_pred
