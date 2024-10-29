from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_homepage_success():
    response = client.get("/status")
    assert response.status_code == 200
