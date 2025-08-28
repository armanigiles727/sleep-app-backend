from datetime import datetime
from pydantic import BaseModel, Field
class SleepSession(BaseModel):
    user_id: str
    session_id: str
    start_at: datetime
    end_at: datetime
    duration_min: int = Field(ge=0)
    created_at: datetime


# NEW: what Flutter expects from /leaderboard
class LeaderboardEntry(BaseModel):
    id: int
    rank: int
    name: str
    hours: float = Field(ge=0)
    avatarUrl: str | None = None
    bio: str | None = None