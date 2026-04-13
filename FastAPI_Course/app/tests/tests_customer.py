from fastapi import status


plan = {"name": "Basic", "price": 12, "descripcion": "Plan básico límitado."}


def test_create_customer(client):
    response = client.post(
        "/customer",
        json={"name": "Jhon Doe", "email": "jhon@example.com", "age": 33},
    )
    assert response.status_code == status.HTTP_201_CREATED


def test_read_customer(client):
    response = client.post(
        "/customer",
        json={"name": "Jhon Doe", "email": "jhon@example.com", "age": 33},
    )
    assert response.status_code == status.HTTP_201_CREATED
    customer_id: int = response.json()["id"]
    response_read = client.get(f"/customer/{customer_id}")
    assert response_read.status_code == status.HTTP_200_OK
    assert response_read.json()["name"] == "Jhon Doe"
