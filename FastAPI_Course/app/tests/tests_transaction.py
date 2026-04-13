from fastapi import status


def test_create_transaction(client):
    response = client.post(
        "/transaction",
        json={
            "amount": 100,
        },
    )
    print("response = " + str(response.status_code))
    assert response.status_code == status.HTTP_201_CREATED
