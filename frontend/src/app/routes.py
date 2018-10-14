# -*- encoding: UTF-8 -*-
import json 

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
    # response = requests.post(app.config["URL"], json=json.dumps(request.form))
    response = 1
    if response.json["status"] == 1:
        status = "dead"
    else:
        status = "alive"
    return render_template('result.html', status=status)
