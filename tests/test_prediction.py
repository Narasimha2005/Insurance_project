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
