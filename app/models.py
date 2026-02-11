from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from datetime import datetime
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)


class PredictionLog(Base):
    __tablename__ = "prediction_logs"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    age = Column(Integer)
    sex = Column(String)
    bmi = Column(Float)
    children = Column(Integer)
    smoker = Column(String)
    region = Column(String)
    predicted_cost = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)


class InsurancePlan(Base):
    __tablename__ = "insurance_plans"
    id = Column(Integer, primary_key=True, index=True)
    plan_name = Column(String)
    min_cost = Column(Float)
    max_cost = Column(Float)
    benefits = Column(String)
