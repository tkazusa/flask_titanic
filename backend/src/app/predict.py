# -*- encoding: UTF-8 -*-
import numpy as np
from sklearn.externals import joblib

MODEL_PATH = "/src/app/models/rf.pkl" 

class Predictor(object):
    """prediction class"""

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data):
        return self.model.predict(data)
