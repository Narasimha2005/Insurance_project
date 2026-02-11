import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 🔥 Force SQLite for tests BEFORE importing app
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

from app.main import app
from app.database import Base, get_db
from app import models

engine = create_engine(
    os.environ["DATABASE_URL"],
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


@pytest.fixture(scope="session", autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()

    plans = [
        models.InsurancePlan(
            plan_name="Silver Plan",
            min_cost=0,
            max_cost=10000,
            benefits="Basic coverage",
        ),
        models.InsurancePlan(
            plan_name="Gold Plan",
            min_cost=10001,
            max_cost=25000,
            benefits="Medium coverage",
        ),
        models.InsurancePlan(
            plan_name="Platinum Plan",
            min_cost=25001,
            max_cost=70000,
            benefits="Premium coverage",
        ),
    ]

    db.add_all(plans)
    db.commit()
    db.close()

    yield

    Base.metadata.drop_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)
