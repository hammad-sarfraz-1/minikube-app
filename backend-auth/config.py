import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "supersecretkey")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "postgresql://user:pass@db:5432/appdb")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
