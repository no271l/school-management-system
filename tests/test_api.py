from fastapi.testclient import TestClient
from api import app

# Create a TestClient instance
client = TestClient(app)

def test_read_pupils():
    response = client.get("/pupils")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_teacher():
    response = client.get("/teachers")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_pupil():
    """Checks if we can create a new pupil via the API."""
    
    # The data we will send (as if we were typing it in the Swagger UI)
    new_pupil_data = {
        "first_name": "Test",
        "last_name": "User",
        "fathers_name": "Automated",
        "age": 15,
        "pupil_class": 1,
        "id_card": "TEST1234"
    }
    
    # We make the POST request by sending the dictionary as JSON
    response = client.post("/pupils", json=new_pupil_data)
    
    # We check if the API accepted the request (200 OK)
    assert response.status_code == 200
    
    # We check if the response contains the data we sent
    data = response.json()
    assert "pupil" in data
    assert data["pupil"]["first_name"] == "Test"


def test_delete_non_existent_pupil():
    """Checks if the API returns 404 when deleting a non-existent pupil."""
    
    # We try to delete a pupil with an ID that doesn't exist
    response = client.delete("/pupils/9999999")
    
    # If the pupil doesn't exist, the API should return 404 (Not Found)
    assert response.status_code == 404
    
    # Optionally: Check the error message
    assert response.json()["detail"] == "Pupil not found."
