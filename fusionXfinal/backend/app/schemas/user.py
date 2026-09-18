from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    full_name: str = Field(..., min_length=2)
    phone: str = Field(..., min_length=7)
    email: EmailStr


class OTPRequest(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None


class OTPVerify(BaseModel):
    email: EmailStr | None = None
    phone: str | None = None
    otp: str = Field(..., min_length=4, max_length=6)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
