from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models
import pandas as pd
import joblib
import os

router = APIRouter()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MODEL_PATH = os.path.join(BASE_DIR, "model", "v1.pkl")

model = joblib.load(MODEL_PATH)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/predict")
def predict(
    user_id: int,
    age: int,
    sex: str,
    bmi: float,
    children: int,
    smoker: str,
    region: str,
    db: Session = Depends(get_db),
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    data = pd.DataFrame(
        [
            {
                "age": age,
                "sex": sex,
                "bmi": bmi,
                "children": children,
                "smoker": smoker,
                "region": region,
            }
        ]
    )

    predicted_cost = float(model.predict(data)[0])

    log = models.PredictionLog(
        user_id=user_id,
        age=age,
        sex=sex,
        bmi=bmi,
        children=children,
        smoker=smoker,
        region=region,
        predicted_cost=predicted_cost,
    )

    db.add(log)
    db.commit()
    db.refresh(log)

    return {
        "prediction_id": log.id,
        "predicted_cost": predicted_cost,
    }
