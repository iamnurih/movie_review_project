from sqlalchemy import Column, Integer, String, Text, DateTime, CheckConstraint
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable = False)
    content = Column(Text, nullable = False)
    rating = Column(Integer, CheckConstraint('rating >=1 AND rating <=5'))
    created_at = Column(DateTime, nullable = False)
