from fastapi import status


def test_create_transaction(client):
    response = client.post("/transaction", json={"amount": 100})
    assert response.status_code == status.HTTP_201_CREATED
