from fastapi import APIRouter, Depends, HTTPException

from app.api.auth import get_current_user

router = APIRouter()


@router.get("/maintenance")
def maintenance(user=Depends(get_current_user)):
    return [{"appliance": "AC - Room 203", "last_cleaned_at": "2026-09-01", "next_cleaning_at": "2026-09-16", "status": "Due soon"}]


@router.post("/maintenance/{maintenance_id}/cleaned")
def mark_cleaned(maintenance_id: int, user=Depends(get_current_user)):
    return {"status": "updated", "maintenance_id": maintenance_id, "next_cleaning_at": "2026-09-30"}
