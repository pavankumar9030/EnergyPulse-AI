from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.core.database import Base


class Building(Base):
    __tablename__ = "buildings"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    building_type = Column(String, nullable=False)
    rooms = Column(Integer, default=0)
    floors = Column(Integer, default=1)
    area_sqft = Column(Float, default=0.0)
    occupants = Column(Integer, default=0)
    operating_hours = Column(String, default="8-18")
    location = Column(String, default="")

    owner = relationship("User", back_populates="buildings")
    zones = relationship("Zone", back_populates="building")
    appliances = relationship("Appliance", back_populates="building")
