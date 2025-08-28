import os
from datetime import timedelta

JWT_SECRET = os.getenv("JWT_SECRET", "change-me-please")  # use a strong secret in prod
JWT_ALG = "HS256"
JWT_EXPIRES = timedelta(hours=12)  # access token lifetime