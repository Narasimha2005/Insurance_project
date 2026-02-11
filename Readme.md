🏥 Medical Insurance API

A production-ready FastAPI REST API for managing insurance users, plans, and premium predictions.

This project demonstrates:

Clean API architecture

Database integration with PostgreSQL

Docker containerization

CI/CD with GitHub Actions

Code quality enforcement

Automated DockerHub deployment

Test coverage enforcement (≥80%)

🚀 Features

✅ User management (CRUD)

✅ Insurance plan management

✅ Premium prediction endpoint

✅ PostgreSQL integration

✅ SQLAlchemy ORM

✅ Pydantic validation

✅ Docker & Docker Compose setup

✅ Automated CI pipeline

✅ DockerHub auto image push

✅ Security scanning (Bandit)

✅ Code linting (Ruff)

✅ Code formatting (Black)

✅ Pytest with coverage enforcement

🛠 Tech Stack
Layer    Technology
API Framework    FastAPI
Database    PostgreSQL
ORM    SQLAlchemy
Validation    Pydantic
Testing    Pytest
Linting    Ruff
Formatting    Black
Security    Bandit
Containerization    Docker
CI/CD    GitHub Actions
📂 Project Structure
medical-insurance-api/
│
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   │
│   └── routes/
│       ├── users.py
│       ├── plans.py
│       └── predictions.py
│
├── tests/
│   ├── conftest.py
│   └── test_*.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── .github/workflows/ci.yml

⚙️ Local Development Setup
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/medical-insurance-api.git
cd medical-insurance-api

2️⃣ Create Virtual Environment
python -m venv venv

Activate

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Environment Variable

Windows:

set DATABASE_URL=postgresql://user:password@localhost:5432/mydb


Linux/Mac:

export DATABASE_URL=postgresql://user:password@localhost:5432/mydb

5️⃣ Run the Application
uvicorn app.main:app --reload


Open in browser:

http://localhost:8000/docs

🐳 Running with Docker (Recommended)
🔹 Using Docker Compose
docker compose up --build


Access:

http://localhost:8000/docs

🔹 Docker Compose Configuration
version: "3.9"

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    ports:
      - "5432:5432"

  api:
    image: <your-dockerhub-username>/medical-insurance-api:latest
    depends_on:
      - postgres
    environment:
      DATABASE_URL: postgresql://user:password@postgres:5432/mydb
    ports:
      - "8000:8000"


⚠ Important:
Inside Docker use postgres as host — never localhost.

🧪 Testing

Run tests:

pytest


Run with coverage:

pytest --cov=app --cov-report=term-missing


Minimum required coverage: 80%

🧹 Code Quality & Security
Ruff (Lint)
ruff check .

Black (Format)
black .

Bandit (Security Scan)
bandit -r app

🔄 CI/CD Pipeline

GitHub Actions automatically performs:

✔ Ruff lint check

✔ Black format check

✔ Bandit security scan

✔ Pytest execution

✔ Coverage enforcement

✔ Docker image build

✔ DockerHub push

🐳 DockerHub Deployment

Image automatically published to:

docker pull <your-dockerhub-username>/medical-insurance-api:latest


Run:

docker run -p 8000:8000 \
-e DATABASE_URL=postgresql://user:password@host.docker.internal:5432/mydb \
<your-dockerhub-username>/medical-insurance-api:latest

📡 API Endpoints
👤 Users
Method    Endpoint
POST    /users
GET    /users
GET    /users/{id}
📋 Plans
Method    Endpoint
POST    /plans
GET    /plans
🔮 Predictions
Method    Endpoint
POST    /predictions
🔐 Environment Variables
Variable    Description
DATABASE_URL    PostgreSQL connection string
🧠 Architectural Highlights

Dependency injection pattern

Modular route structure

Environment-based configuration

Database session management

Clean separation of models, schemas, and business logic

Container-ready configuration

Production-safe startup handling





