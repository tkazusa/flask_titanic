# -*- encoding: UTF-8 -*-
import json


def test_prediction(test_client, test_data):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.post('/', json=json.dumps(test_data), headers={'Content-Type': 'application/json'})
    assert response.status_code == 200

    status = response.data
    assert status == b'{"status":1}' or b'{"status":0}'


def test_not_found(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/not/found' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/api/not/found')
    assert response.status_code == 404
