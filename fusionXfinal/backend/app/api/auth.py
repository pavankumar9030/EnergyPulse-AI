from datetime import datetime, timedelta

import jwt
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import OTPRequest, OTPVerify, TokenResponse, UserRegister
from app.services.otp import otp_service

router = APIRouter()
security = HTTPBearer()


def create_token(user_id: int) -> str:
    payload = {"sub": str(user_id), "exp": datetime.utcnow() + timedelta(days=7)}
    return jwt.encode(payload, settings.jwt_secret, algorithm="HS256")


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=["HS256"])
    except jwt.PyJWTError as exc:  # type: ignore[attr-defined]
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from exc
    user = db.query(User).filter(User.id == int(payload["sub"])).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user


@router.post("/register", response_model=TokenResponse)
def register_user(payload: UserRegister, db: Session = Depends(get_db)):
    if db.query(User).filter((User.email == payload.email) | (User.phone == payload.phone)).first():
        raise HTTPException(status_code=400, detail="User already exists")
    user = User(full_name=payload.full_name, email=str(payload.email), phone=payload.phone, is_verified=True)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"access_token": create_token(user.id), "token_type": "bearer"}


@router.post("/send-otp")
def send_otp(payload: OTPRequest, db: Session = Depends(get_db)):
    contact = payload.email or payload.phone
    if not contact:
        raise HTTPException(status_code=400, detail="Email or phone is required")
    if otp_service.rate_limit_exceeded(contact):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    if not otp_service.can_send(contact):
        raise HTTPException(status_code=429, detail="Please wait before requesting another OTP")
    code = otp_service.generate(contact)
    otp_service.register_attempt(contact)
    return {"status": "success", "message": "OTP sent", "otp": code if settings.otp_provider == "mock" else None}


@router.post("/verify-otp")
def verify_otp(payload: OTPVerify, db: Session = Depends(get_db)):
    contact = payload.email or payload.phone
    if not contact:
        raise HTTPException(status_code=400, detail="Email or phone is required")
    if otp_service.rate_limit_exceeded(contact):
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    if not otp_service.verify(contact, payload.otp):
        raise HTTPException(status_code=401, detail="Invalid or expired OTP")
    user = db.query(User).filter((User.email == str(payload.email)) | (User.phone == payload.phone)).first()
    if user:
        user.is_verified = True
        db.commit()
    return {"status": "verified"}


@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {"id": user.id, "full_name": user.full_name, "email": user.email, "phone": user.phone}


@router.post("/logout")
def logout():
    return {"status": "logged out"}
