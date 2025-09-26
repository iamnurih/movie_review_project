import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()

class Config:
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "RIVERHOME")
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    database = os.getenv("DB_DATABASE", "movie_review")

    if not TURSO_DATABASE_URL and not TURSO_AUTH_TOKEN:
        SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
        CONNECT_ARGS ={"auth_token": TURSO_AUTH_TOKEN}

    else:
       SQLALCHEMY_DATABASE_URI = (
           f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
       )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
)

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))