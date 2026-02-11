def test_prediction(client):
    user = client.post(
        "/users",
        params={"name": "Test User", "email": "test1@example.com"},
    ).json()

    response = client.post(
        "/predict",
        params={
            "user_id": user["id"],
            "age": 45,
            "sex": "female",
            "bmi": 28.5,
            "children": 2,
            "smoker": "no",
            "region": "southwest",
        },
    )

    assert response.status_code == 200
    assert "predicted_cost" in response.json()


def test_prediction_invalid_user(client):
    response = client.post(
        "/predict",
        params={
            "user_id": 9999,
            "age": 30,
            "sex": "male",
            "bmi": 25,
            "children": 0,
            "smoker": "no",
            "region": "northwest",
        },
    )
    assert response.status_code in (400, 404)


def test_prediction_missing_fields(client):
    response = client.post("/predict", params={"user_id": 1})
    assert response.status_code in (400, 422)
