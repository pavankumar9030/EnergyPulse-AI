from datetime import date

from pydantic import BaseModel, Field


class ApplianceCreate(BaseModel):
    appliance_type: str
    appliance_name: str
    quantity: int = 1
    brand: str | None = None
    model: str | None = None
    age_years: int = 0
    purchase_date: date | None = None
    star_rating: str = "3 Star"
    rated_power_kw: float = 0.0
    usage_hours_per_day: float = 0.0
    typical_usage_time: str = ""
    building_zone: str = ""
    zone_id: int | None = None


class ApplianceUpdate(ApplianceCreate):
    pass
