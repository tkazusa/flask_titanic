# -*- encoding: UTF-8 -*-
import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    URL = "http://backend:8081"
    headers = {'Content-Type': 'application/json'}
