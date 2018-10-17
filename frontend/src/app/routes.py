# -*- encoding: UTF-8 -*-
import json 
import ast

import requests
from flask import Flask, request, render_template
from app import app
from app.forms import InputForm


@app.route('/', methods=["GET"])
def input():
    form = InputForm()
    return render_template('input.html', title='Input', form=form)


@app.route('/', methods=["POST"])
def result():
    response = requests.post(app.config["URL"], json=json.dumps(request.form))
    status = response.content.decode()
    dict_status = ast.literal_eval(status)

    if dict_status['status'] == 0:
        status = 'dead'
    else:
        status = 'alive'

    return render_template('result.html', status=status)

