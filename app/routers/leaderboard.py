from typing import List, Literal
from fastapi import APIRouter, Query
from app.models import LeaderboardEntry

router = APIRouter(prefix="/leaderboard", tags=["leaderboard"])

# Demo data; replace with DB later
DAY_DATA = [
    {"id": 1, "name": "Armani G.", "hours": 8.2, "avatarUrl": "https://i.pravatar.cc/150?img=15", "bio": "Full-stack dev. Loves sleep tracking, kettlebells, and matcha."},
    {"id": 2, "name": "Maya L.",  "hours": 7.9, "avatarUrl": "https://i.pravatar.cc/150?img=32", "bio": "RN enthusiast. Night owl turned early bird."},
    {"id": 3, "name": "J. Chen",  "hours": 7.6, "avatarUrl": "https://i.pravatar.cc/150?img=5",  "bio": "Data viz nerd. Dreams in charts."},
    {"id": 4, "name": "R. Patel", "hours": 7.4, "avatarUrl": "https://i.pravatar.cc/150?img=8",  "bio": "Backend whisperer. Loves long hikes and longer naps."},
]

WEEK_DATA = [
    {"id": 1, "name": "Armani G.", "hours": 54.3, "avatarUrl": "https://i.pravatar.cc/150?img=15", "bio": "Full-stack dev. Loves sleep tracking, kettlebells, and matcha."},
    {"id": 3, "name": "J. Chen",  "hours": 53.1, "avatarUrl": "https://i.pravatar.cc/150?img=5",  "bio": "Data viz nerd. Dreams in charts."},
    {"id": 2, "name": "Maya L.",  "hours": 51.6, "avatarUrl": "https://i.pravatar.cc/150?img=32", "bio": "RN enthusiast. Night owl turned early bird."},
    {"id": 4, "name": "R. Patel", "hours": 49.8, "avatarUrl": "https://i.pravatar.cc/150?img=8",  "bio": "Backend whisperer. Loves long hikes and longer naps."},
]

def with_ranks(rows: list[dict]) -> list[dict]:
    rows = sorted(rows, key=lambda r: r["hours"], reverse=True)
    for i, r in enumerate(rows, start=1):
        r["rank"] = i
        r["hours"] = round(float(r["hours"]), 1)
    return rows

@router.get("", response_model=List[LeaderboardEntry])
def leaderboard(period: Literal["day", "week"] = Query(default="day")):
    data = DAY_DATA if period == "day" else WEEK_DATA
    return with_ranks([r.copy() for r in data])