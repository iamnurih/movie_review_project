import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Turso 설정
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

    # MySQL 설정
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "RIVERHOME")
    host = os.getenv("DB_HOST", "localhost")
    port = 3306
    database = os.getenv("DB_NAME", "movie_review")

    # 데이터베이스 URI 설정
    # Vercel 환경에서는 Turso를, 로컬에서는 MySQL을 사용
    if os.getenv("VERCEL"):
        # Vercel 환경에서 Turso 사용
        if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
            SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
            CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}
            print("\n[INFO] Using Turso Database (Vercel)...\n")
        else:
            # Vercel에서 Turso 환경변수가 없으면 SQLite 사용
            SQLALCHEMY_DATABASE_URI = "sqlite:///movie_review.db"
            CONNECT_ARGS = {}
            print("\n[INFO] Using SQLite Database (Vercel)...\n")
    else:
        # 로컬에서는 MySQL 사용
        print("\n[INFO] Using MySQL Database (Local)...\n")
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        CONNECT_ARGS = {}

    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Config 인스턴스 생성
config = Config()

# 엔진과 세션 생성
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True, connect_args=config.CONNECT_ARGS)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))