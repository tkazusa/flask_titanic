# -*- encoding: UTF-8 -*-
import json

import requests
import pytest
from app import app


@pytest.fixture(scope='module')
def test_client():
    testing_client = app.test_client()
    yield testing_client

@pytest.fixture(scope='module')
def test_data():
    data = {
        "Name": 'Taketoshi, Mr. Kazusa',
        "Sex": 0,
        "Age": 25,
        "Embarked": 'C',
        "Pclass": '1',
        "SibSP": '1',
        "Parch": '1',
        "Cabin": 'C123',
        "Tciket": '113903'
    }
    testing_data = json.dumps(data)
    yield testing_data
