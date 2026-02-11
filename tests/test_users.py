def test_create_user(client):
    response = client.post(
        "/users",
        params={"name": "Test User", "email": "testuser@example.com"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"


def test_duplicate_user_email(client):
    client.post(
        "/users",
        params={"name": "Dup", "email": "dup@example.com"},
    )
    response = client.post(
        "/users",
        params={"name": "Dup2", "email": "dup@example.com"},
    )
    assert response.status_code in (400, 409, 422)


def test_get_users(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_single_user(client):
    user = client.post(
        "/users",
        params={"name": "Single", "email": "single@example.com"},
    ).json()

    response = client.get(f"/users/{user['id']}")
    assert response.status_code == 200


def test_get_nonexistent_user(client):
    response = client.get("/users/9999")
    assert response.status_code in (400, 404)
