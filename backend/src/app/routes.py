# -*- encoding: UTF-8 -*-
import json 

from flask import Flask, jsonify, request
import pandas as pd

from app import app
from app.people import People 


@app.route('/', methods=['POST'])
def post():
    data = json.loads(request.json)
    INPUT_DATA = pd.DataFrame({
        'Name':     [data['Name']],
        'Sex':      [data['Sex']],
        'Age':      [data['Age']],
        'Embarked': [data['Embarked']],
        'Pclass':   [data['Pclass']],
        'SibSp':    [data['SibSp']],
        'Parch':    [data['Parch']],
        'Cabin':    [data['Cabin']],
        'Ticket':   [data['Ticket']]
    })
    people = People(INPUT_DATA)
    status = people.status_predict().tolist()[0]
    response = jsonify({"status": status})
    return response

