# -*- encoding: UTF-8 -*-
from preprocess import preprocess
from predict import Predictor


class People:
    def __init__(self, INPUT_DATA):
        self.data = INPUT_DATA

    def status_prediction(self):
        PreprocessedData = preprocess(self.data)
        model = Predictor()
        status = model.predict(PreprocessedData)
        return status
