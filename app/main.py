from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # <-- make sure this import is correct
from .routers import health, users, sleep, leaderboard

app = FastAPI(title="Sleep App API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # tighten later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(users.router)
app.include_router(sleep.router)
app.include_router(leaderboard.router)