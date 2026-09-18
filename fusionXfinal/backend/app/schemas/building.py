from pydantic import BaseModel, Field


class BuildingCreate(BaseModel):
    name: str = Field(..., min_length=2)
    building_type: str
    rooms: int = 0
    floors: int = 1
    area_sqft: float = 0.0
    occupants: int = 0
    operating_hours: str = "8-18"
    location: str = ""


class BuildingUpdate(BuildingCreate):
    pass
