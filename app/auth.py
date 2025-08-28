# auth.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from google.oauth2 import id_token
from google.auth.transport import requests
from .auth_utils import create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])
security = HTTPBearer()

GOOGLE_CLIENT_IDS = {
    "ios": "367244143502-134j94jrrb8fjnk7c3miv6p8n2jqumms.apps.googleusercontent.com"
}

@router.post("/google")
def verify_google_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        info = id_token.verify_oauth2_token(token, requests.Request())

        aud = info.get("aud")
        if aud not in GOOGLE_CLIENT_IDS.values():
            raise HTTPException(status_code=401, detail="Invalid audience")

        # identify the user in YOUR system (email or your own user_id)
        email = info.get("email")
        name = info.get("name")
        picture = info.get("picture")

        # TODO: upsert user in DB here if you want persistence

        access_token = create_access_token(sub=email, extra={"name": name, "picture": picture})
        return {
            "access_token": access_token,
            "token_type": "bearer",
            "user": {"email": email, "name": name, "picture": picture},
        }
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid Google token")