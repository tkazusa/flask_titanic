# -*- encoding: UTF-8 -*-
from flask import render_template
from app import app
from app.forms import InputForm

@app.route('/')
def input():
    form = InputForm()
    return render_template('input.html', title='Input', form=form)
