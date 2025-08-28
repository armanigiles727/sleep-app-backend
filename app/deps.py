from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from .config import JWT_SECRET, JWT_ALG

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALG])
        # payload has "sub", optional "name", "picture"
        return {
            "email": payload.get("sub"),
            "name": payload.get("name"),
            "picture": payload.get("picture"),
        }
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Session expired")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")