from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.core.database import get_db
from app.models.appliance import Appliance
from app.models.building import Building
from app.schemas.appliance import ApplianceCreate

router = APIRouter()


@router.post("/appliances")
def create_appliance(payload: ApplianceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building = db.query(Building).filter(Building.id == 1, Building.user_id == current_user.id).first()
    if not building:
        building = db.query(Building).filter(Building.user_id == current_user.id).first()
    if not building:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Create a building before adding appliances")
    appliance = Appliance(building_id=building.id, **payload.model_dump())
    db.add(appliance)
    db.commit()
    db.refresh(appliance)
    return appliance


@router.get("/appliances")
def list_appliances(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    buildings = [b.id for b in db.query(Building).filter(Building.user_id == current_user.id).all()]
    return db.query(Appliance).filter(Appliance.building_id.in_(buildings)).all()


@router.put("/appliances/{appliance_id}")
def update_appliance(appliance_id: int, payload: ApplianceCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    appliance = db.query(Appliance).join(Building).filter(Appliance.id == appliance_id, Building.user_id == current_user.id).first()
    if not appliance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appliance not found")
    for field, value in payload.model_dump().items():
        setattr(appliance, field, value)
    db.commit()
    return appliance


@router.delete("/appliances/{appliance_id}")
def delete_appliance(appliance_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    appliance = db.query(Appliance).join(Building).filter(Appliance.id == appliance_id, Building.user_id == current_user.id).first()
    if not appliance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Appliance not found")
    db.delete(appliance)
    db.commit()
    return {"deleted": True}
