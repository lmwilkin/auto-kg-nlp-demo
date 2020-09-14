from starlette.testclient import TestClient

from app.api import app

client = TestClient(app)


def test_ping():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}