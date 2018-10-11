# -*- encoding: UTF-8 -*-
from flask import Flask, jsonify, request
import pandas as pd

from app import app
from people import People 


@app.route('/', methods=['POST'])
def post():
    data = request.json
    INPUT_DATA = pd.read_json(data)
    people = People(INPUT_DATA)
    status = people.status_predict()

    response = jsonify(status)
    response.status_code = 200
    return response

