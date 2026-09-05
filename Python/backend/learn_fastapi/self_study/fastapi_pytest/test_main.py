from fastapi.testclient import TestClient

from .main import App

client = TestClient(App().getApp())


def test_read_main():
    response = client.get("http://127.0.0.1:8000/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}
