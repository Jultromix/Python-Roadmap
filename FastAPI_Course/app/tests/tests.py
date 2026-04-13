from fastapi.testclient import TestClient


def test_client(client):
    # assert type(client) == "dsadsa"
    assert type(client) == TestClient
