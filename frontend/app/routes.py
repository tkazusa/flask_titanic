# -*- encoding: UTF-8 -*-
import requests
import json 

from flask import Flask, request, render_template
from app import app
from app.forms import InputForm


@app.route('/', methods=["GET"])
def input():
    form = InputForm()
    return render_template('input.html', title='Input', form=form)


@app.route('/', methods=["POST"])
def result():
    # response = requests.post(app.config["URL"], data=json.dumps(request.form), headers=app.config["headers"])
    response = 1
    if response == 1:
        status = "ざんねーん、死んじゃうよ！"
    else:
        status = "良かったね！生き残るってさ！"
    return render_template('result.html', status=status)
