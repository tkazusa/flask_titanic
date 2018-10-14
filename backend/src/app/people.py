# -*- encoding: UTF-8 -*-
from app.preprocess import preprocess
from app.predict import Predictor


class People:
    def __init__(self, INPUT_DATA):
        self.data = INPUT_DATA

    def status_predict(self):
        PreprocessedData = preprocess(self.data)
        model = Predictor()
        status = model.predict(PreprocessedData)
        return status
