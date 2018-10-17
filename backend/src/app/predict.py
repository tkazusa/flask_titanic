# -*- encoding: UTF-8 -*-
import os
from sklearn.externals import joblib


MODEL_PATH = os.path.normpath(os.path.join(os.path.abspath(__name__),
                                           '../app/models/rf.pkl'))


class Predictor(object):
    """prediction class"""

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, data):
        return self.model.predict(data)
