# 💤 Sleep App API (FastAPI Backend)

This is the backend API for the Sleep App project, built with **FastAPI**. It powers features such as user sleep tracking, leaderboard rankings, and secure Google OAuth sign-in.

---

## 🚀 Features

- ✅ Google Sign-In (OAuth2 with JWT token validation)
- 📈 Leaderboard endpoint (sorted by sleep hours)
- 🧑‍💻 User profile: email, avatar, bio
- ⚡ FastAPI with async endpoints
- 🗄️ PostgreSQL database with SQLAlchemy or Tortoise ORM
- 🔐 Token-based authentication
- 📄 CORS and security middleware
- ☁️ Ready for deployment on platforms like AWS EC2 or Heroku

---

## 🛠 Tech Stack

- **Framework:** FastAPI
- **Auth:** Google OAuth2 (ID Token validation)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy / Tortoise ORM (your choice)
- **Other:** Pydantic, Uvicorn, Python 3.10+

---

## 📦 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/armanigiles727/sleep-app-api.git
cd sleep-app-api
