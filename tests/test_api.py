from fastapi.testclient import TestClient
from api import app

# Create a TestClient instance
client = TestClient(app)

def test_read_pupils():
    response = client.get("/pupils")
    assert response.status_code == 200
    assert isinstance(response.json(), list)