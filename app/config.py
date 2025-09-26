import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Config:
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "RIVERHOME")
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", "3306"))
    database = os.getenv("DB_NAME", "movie_review")

    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=True)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))