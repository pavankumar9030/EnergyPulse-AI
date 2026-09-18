from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class Appliance(Base):
    __tablename__ = "appliances"

    id = Column(Integer, primary_key=True, index=True)
    building_id = Column(Integer, ForeignKey("buildings.id"), nullable=False)
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=True)
    appliance_type = Column(String, nullable=False)
    appliance_name = Column(String, nullable=False)
    quantity = Column(Integer, default=1)
    brand = Column(String, nullable=True)
    model = Column(String, nullable=True)
    age_years = Column(Integer, default=0)
    purchase_date = Column(Date, nullable=True)
    star_rating = Column(String, default="3 Star")
    rated_power_kw = Column(Float, default=0.0)
    usage_hours_per_day = Column(Float, default=0.0)
    typical_usage_time = Column(String, default="")
    building_zone = Column(String, default="")

    building = relationship("Building", back_populates="appliances")
    zone = relationship("Zone", back_populates="appliances")
