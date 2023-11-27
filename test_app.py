# test_app.py

import pytest
from app import app

@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    return app.test_client()

def test_hello(client):
    """Test the / endpoint."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, Flask!' in response.data
