from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.auth import get_current_user
from app.core.database import get_db
from app.models.building import Building
from app.schemas.building import BuildingCreate

router = APIRouter()


@router.post("/buildings")
def create_building(payload: BuildingCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building = Building(user_id=current_user.id, **payload.model_dump())
    db.add(building)
    db.commit()
    db.refresh(building)
    return building


@router.get("/buildings")
def list_buildings(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return db.query(Building).filter(Building.user_id == current_user.id).all()


@router.get("/buildings/{building_id}")
def get_building(building_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building = db.query(Building).filter(Building.id == building_id, Building.user_id == current_user.id).first()
    if not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
    return building


@router.put("/buildings/{building_id}")
def update_building(building_id: int, payload: BuildingCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    building = db.query(Building).filter(Building.id == building_id, Building.user_id == current_user.id).first()
    if not building:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Building not found")
    for field, value in payload.model_dump().items():
        setattr(building, field, value)
    db.commit()
    return building
