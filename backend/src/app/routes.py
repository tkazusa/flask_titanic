# -*- encoding: UTF-8 -*-
import json 

from flask import Flask, jsonify, request
import pandas as pd

from app import app
from app.people import People 


@app.route('/', methods=['POST'])
def post():
    data = json.loads(request.json)
    INPUT_DATA = pd.DataFrame(data, index=[0]).drop(columns="csrf_token")
    people = People(INPUT_DATA)
    status = people.status_predict()
    response = jsonify({"status":status})
    return response

