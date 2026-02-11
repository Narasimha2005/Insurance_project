def test_create_user(client):
    response = client.post(
        "/users",
        params={"name": "Test User", "email": "testuser@example.com"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_single_user(client):
    response = client.get("/users/1")
    assert response.status_code == 200
