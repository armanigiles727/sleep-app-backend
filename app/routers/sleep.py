from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
import uuid

from app.deps import get_current_user
from app.db import put_sleep_session

router = APIRouter(prefix="/sleep", tags=["sleep"])

@router.post("")
def record_sleep(user = Depends(get_current_user)):
    """
    Baby-step stub:=
    - Creates a 0-minute session with start=end=now
    - Stores in mock memory (default) or DynamoDB if DB_MODE=aws
    """
    now = datetime.utcnow().isoformat()
    item = {
        "user_id": user["user_id"],
        "session_id": str(uuid.uuid4()),
        "start_at": now,
        "end_at": now,
        "duration_min": 0,
        "created_at": now,
    }
    try:
        put_sleep_session(item)
        return {"ok": True, "session_id": item["session_id"], "mode": "mock-or-aws"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"store_failed: {e}")