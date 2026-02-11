from fastapi import FastAPI
from sqlalchemy.orm import Session
from app.database import engine, Base, SessionLocal
from app.routes import users, predictions, plans
from app import models

app = FastAPI(title="Medical Insurance Prediction API")


def seed_insurance_plans():
    db: Session = SessionLocal()
    try:
        existing = db.query(models.InsurancePlan).count()
        if existing == 0:
            plans_data = [
                {
                    "plan_name": "Silver Plan",
                    "min_cost": 0,
                    "max_cost": 10000,
                    "benefits": "Basic hospitalization, limited coverage",
                },
                {
                    "plan_name": "Gold Plan",
                    "min_cost": 10001,
                    "max_cost": 25000,
                    "benefits": "Extended coverage, diagnostics, OPD",
                },
                {
                    "plan_name": "Platinum Plan",
                    "min_cost": 25001,
                    "max_cost": 70000,
                    "benefits": "Premium coverage, zero waiting period, ICU",
                },
            ]

            for plan in plans_data:
                db.add(models.InsurancePlan(**plan))

            db.commit()
    finally:
        db.close()


# 🔥 Proper startup lifecycle
@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    seed_insurance_plans()


# Include routers
app.include_router(users.router)
app.include_router(predictions.router)
app.include_router(plans.router)


@app.get("/health")
def health():
    return {"status": "OK"}
