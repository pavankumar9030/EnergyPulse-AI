from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.auth import router as auth_router
from app.api.buildings import router as buildings_router
from app.api.appliances import router as appliances_router
from app.api.readings import router as readings_router
from app.api.analytics import router as analytics_router
from app.api.maintenance import router as maintenance_router
from app.api.reports import router as reports_router
from app.core.config import settings
from app.core.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_url, "http://localhost:3000", "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/auth", tags=["auth"])
app.include_router(buildings_router, prefix="/api", tags=["buildings"])
app.include_router(appliances_router, prefix="/api", tags=["appliances"])
app.include_router(readings_router, prefix="/api", tags=["readings"])
app.include_router(analytics_router, prefix="/api", tags=["analytics"])
app.include_router(maintenance_router, prefix="/api", tags=["maintenance"])
app.include_router(reports_router, prefix="/api", tags=["reports"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
