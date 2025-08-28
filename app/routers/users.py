from fastapi import APIRouter, Depends
from app.deps import get_current_user

router = APIRouter(prefix="/me", tags=["me"])

@router.get("")
def me(user = Depends(get_current_user)):
    return user