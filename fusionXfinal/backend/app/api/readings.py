from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.core.database import get_db
from app.models.building import Building
from app.models.appliance import Appliance

router = APIRouter()


@router.post("/readings")
def create_reading(payload: dict, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building = db.query(Building).filter(Building.user_id == current_user.id).first()
    if not building:
        raise HTTPException(status_code=400, detail="Create a building before adding readings")
    appliance = db.query(Appliance).filter(Appliance.building_id == building.id).first()
    if not appliance:
        raise HTTPException(status_code=400, detail="Add an appliance before creating readings")
    return {"status": "ok", "building_id": building.id, "appliance_id": appliance.id, "reading": payload}


@router.get("/readings")
def list_readings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building_ids = [b.id for b in db.query(Building).filter(Building.user_id == current_user.id).all()]
    return {"buildings": building_ids, "readings": []}
