# -*- encoding: UTF-8 -*-
import pytest
from app import app


@pytest.fixture(scope='module')
def test_client():
    testing_client = app.test_client()
    yield testing_client


@pytest.fixture(scope='module')
def test_data():
    testing_data = {
        "Name": 'Taketoshi, Mr. Kazusa',
        "Sex": 0,
        "Age": 25,
        "Embarked": 'C',
        "Pclass": '1',
        "SibSp": '1',
        "Parch": '1',
        "Cabin": 'C123',
        "Ticket": '113903'
    }
    yield testing_data
