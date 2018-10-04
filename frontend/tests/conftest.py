# -*- encoding: UTF-8 -*-
import requests
import pytest
from app import app


@pytest.fixture(scope='module')
def test_client():
    testing_client = app.test_client()
    yield testing_client


@pytest.fixture()
def no_mlmodel(mocker):
    mocker.patch.object(requests.post(), 'prediction', return_value=1)


