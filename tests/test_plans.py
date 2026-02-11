def test_get_plans(client):
    response = client.get("/plans")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_recommended_plan(client):
    user = client.post(
        "/users",
        params={"name": "Plan User", "email": "plan@example.com"},
    ).json()

    client.post(
        "/predict",
        params={
            "user_id": user["id"],
            "age": 60,
            "sex": "male",
            "bmi": 30,
            "children": 2,
            "smoker": "yes",
            "region": "southeast",
        },
    )

    response = client.get("/recommended-plan", params={"user_id": user["id"]})
    assert response.status_code == 200
    assert "recommended_plan" in response.json()
