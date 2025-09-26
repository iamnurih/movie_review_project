import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

load_dotenv()


class Config:
    TURSO_DATABASE_URL = os.getenv("TURSO_DATABASE_URL")
    TURSO_AUTH_TOKEN = os.getenv("TURSO_AUTH_TOKEN")

    if TURSO_DATABASE_URL and TURSO_AUTH_TOKEN:
        # .env에 값이 있을 시에만 Turso를 사용하도록 설정
        # Turso의 SQLALCHEMY_DATABASE_URI
        SQLALCHEMY_DATABASE_URI = f"sqlite+libsql://{TURSO_DATABASE_URL}?secure=true"
        CONNECT_ARGS = {"auth_token": TURSO_AUTH_TOKEN}
    else:
        # Turso 정보가 없거나 에러가 발생한다면 로컬 db를 사용하도록 설정
        print("\n[INFO] No Turso Setup: Use local db...\n")

        # instance 폴더 경로
        INSTANCE_DIR = os.path.join(os.path.dirname(__file__), "..", "instance")

        # 폴더가 없으면 생성
        os.makedirs(INSTANCE_DIR, exist_ok=True)

        SQLALCHEMY_DATABASE_URI = "sqlite:///instance/reviews.db"
        CONNECT_ARGS = {"check_same_thread": False}


engine = create_engine(
    Config.SQLALCHEMY_DATABASE_URI,
    echo=True,
    connect_args=Config.CONNECT_ARGS,
)

SessionLocal = scoped_session(sessionmaker(bind=engine, autoflush=False, autocommit=False))