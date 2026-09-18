# Smart Energy

AI-based building energy demand forecasting and consumption optimization system.

## Overview

This project is a full-stack application for managing building energy usage, forecasting demand, detecting anomalies, recommending optimizations, and generating PDF reports.

## Architecture

- Frontend: React + TypeScript + Vite + Tailwind CSS + Recharts
- Backend: FastAPI + SQLAlchemy + Pydantic
- Database: PostgreSQL-ready, SQLite for local development
- Authentication: JWT with OTP support and mock/local provider mode

## Repository structure

- backend/
- frontend/
- database/
- docs/
- .env.example
- docker-compose.yml
- Dockerfile
- README.md

## Local setup

1. Create environment file:
   cp .env.example .env
2. Install backend dependencies:
   cd backend && python -m pip install -r requirements.txt
3. Start backend:
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
4. Frontend:
   cd frontend && npm install && npm run dev

## Docker setup

```bash
docker compose up --build
```

## Database

SQLite is used for local default development. The backend is structured to use PostgreSQL in production by switching DATABASE_URL.

## Running tests

```bash
cd backend && pytest -q
```

## API docs

Open http://localhost:8000/docs

## Demo walkthrough

1. Register a user.
2. Send OTP and verify.
3. Create a building and add appliances.
4. View forecast, anomalies, recommendations, and maintenance reminders.
5. Generate a report.

## Security notes

- Never commit real secrets.
- JWT secret must be configured in .env.
- OTP provider is set through environment variables.
