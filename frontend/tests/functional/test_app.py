# -*- encoding: UTF-8 -*-
import pytest
from app import app

def test_get_route(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200

    
def test_not_found(test_client):
    """
    GIVEN a Flask application
    WHEN the '/api/not/found' page is requested (GET)
    THEN check the response is invalid
    """
    response = test_client.get('/api/not/found')
    assert response.status_code == 404

    
def test_post_inputdata(test_client):
    """test for post"""
    response = test_client.post(
        '/',
        data={"submit": "Send",
              "parch": "1",
              "age": "1",
              "ticket": "test_tciket_number",
              "embarked": "C",
              "cabin": "test_cabin_number",
              "sibsp": "1",
              "name": "Mr, Taketoshi Kazusa",
              "sex": "0",
              "pclass": "1"}
    )
    assert response.status_code == 200

