import random
import time
from collections import defaultdict

OTP_STORE: dict[str, dict] = {}
RATE_LIMIT: dict[str, int] = defaultdict(int)


class OTPService:
    def __init__(self, provider: str = "mock"):
        self.provider = provider

    def generate(self, contact: str) -> str:
        code = str(random.randint(100000, 999999))
        OTP_STORE[contact] = {"otp": code, "expires_at": time.time() + 300, "attempts": 0, "last_requested": time.time()}
        return code

    def verify(self, contact: str, otp: str) -> bool:
        record = OTP_STORE.get(contact)
        if not record:
            return False
        if time.time() > record["expires_at"]:
            return False
        if record["attempts"] >= 3:
            return False
        if record["otp"] != otp:
            record["attempts"] += 1
            return False
        return True

    def can_send(self, contact: str) -> bool:
        now = time.time()
        record = OTP_STORE.get(contact)
        if not record:
            return True
        return now - record["last_requested"] >= 60

    def rate_limit_exceeded(self, contact: str) -> bool:
        return RATE_LIMIT.get(contact, 0) >= 5

    def register_attempt(self, contact: str):
        RATE_LIMIT[contact] = RATE_LIMIT.get(contact, 0) + 1

    def clear(self, contact: str):
        OTP_STORE.pop(contact, None)
        RATE_LIMIT.pop(contact, None)


otp_service = OTPService()
