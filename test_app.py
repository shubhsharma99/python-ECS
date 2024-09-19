import pytest
from app import app  # Import your application


@pytest.fixture
def client():
    """Create a test client for the app."""
    
    with app.test_client() as client:
        yield client


def test_hello(client):
    """Test the hello endpoint."""
    
    response = client.get('/')
    assert response.data == b'Hello, World!'
    assert response.status_code == 200
