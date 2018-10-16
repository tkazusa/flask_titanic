# -*- encoding: UTF-8 -*-
import pytest
from app import app

def test_prediction(test_client, test_data):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    #response = test_client.post('/', data=test_data, headers={'Content-Type': 'application/json'})
    #print(response.data)
    #assert response.status_code == 200
    #assert response.json()['status'] == 0 or 1


def test_not_found(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/not/found' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/api/not/found')
    assert response.status_code == 404
