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
    if not TURSO_DATABASE_URL and not TURSO_AUTH_TOKEN:
        # .env에 값이 있을 시에만 Turso를 사용하도록 설정
        SQLALCHEMY_DATABASE_URI = f"sqlite+{TURSO_DATABASE_URL}?secure=true"
        CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}
    else:
        print("\n[INFO] Using MySQL Database...\n")
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"
        CONNECT_ARGS = {}

    SQLALCHEMY_TRACK_MODIFICATIONS = False

# Config 인스턴스 생성
config = Config()

# 엔진과 세션 생성
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True, connect_args=config.CONNECT_ARGS)
SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))