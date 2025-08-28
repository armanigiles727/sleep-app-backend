from fastapi.testclient import TestClient
from app.main import app

def test_leaderboard_stub():
    client = TestClient(app)
    r = client.get("/leaderboard")
    assert r.status_code == 200
    assert "leaders" in r.json()