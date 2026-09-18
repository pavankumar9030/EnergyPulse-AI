from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import relationship

from app.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=True)
    is_verified = Column(Boolean, default=False)
    otp_secret = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=True)

    buildings = relationship("Building", back_populates="owner")
