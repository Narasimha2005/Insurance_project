from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/plans")
def get_all_plans(db: Session = Depends(get_db)):
    return db.query(models.InsurancePlan).all()


@router.get("/plans/{plan_id}")
def get_plan(plan_id: int, db: Session = Depends(get_db)):
    plan = (
        db.query(models.InsurancePlan)
        .filter(models.InsurancePlan.id == plan_id)
        .first()
    )

    if not plan:
        raise HTTPException(status_code=404, detail="Plan not found")

    return plan


@router.get("/recommended-plan")
def recommend_plan(user_id: int, db: Session = Depends(get_db)):
    prediction = (
        db.query(models.PredictionLog)
        .filter(models.PredictionLog.user_id == user_id)
        .order_by(models.PredictionLog.created_at.desc())
        .first()
    )

    if not prediction:
        raise HTTPException(status_code=404, detail="No predictions found")

    plan = (
        db.query(models.InsurancePlan)
        .filter(
            models.InsurancePlan.min_cost <= prediction.predicted_cost,
            models.InsurancePlan.max_cost >= prediction.predicted_cost,
        )
        .first()
    )

    if not plan:
        raise HTTPException(status_code=404, detail="No matching plan")

    return {
        "user_id": user_id,
        "latest_predicted_cost": prediction.predicted_cost,
        "recommended_plan": plan.plan_name,
        "benefits": plan.benefits,
    }
