from datetime import datetime, timezone, timedelta
import jwt
from .config import JWT_SECRET, JWT_ALG, JWT_EXPIRES

def create_access_token(sub: str, extra: dict | None = None):
    now = datetime.now(timezone.utc)
    payload = {
        "sub": sub,           # subject (your internal user id or email)
        "iat": int(now.timestamp()),
        "exp": int((now + JWT_EXPIRES).timestamp()),
        **(extra or {}),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALG)

def verify_access_token(token: str):
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])