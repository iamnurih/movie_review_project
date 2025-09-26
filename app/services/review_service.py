from app.config import SessionLocal
from app.models import Review

def get_all_reviews():
    session = SessionLocal()
    try:
        reviews = session.query(Review).all()
        return reviews
    finally:
        session.close()

def create_review(review):
    session = SessionLocal()
    try:
        session.add(review)
        session.commit()
        session.refresh(review)
        return review
    finally:
        session.close()

def get_review_by_id(review_id):
    session = SessionLocal()
    try:
        review = session.query(Review).filter(Review.id == review_id).first()
        if not review:
            return None
        return review
    finally:
        session.close()


def update_review(review_id, title=None, content=None, rating=None):
    session = SessionLocal()
    try:
        review = session.query(Review).filter(Review.id == review_id).first()
        if not review:
            return None

        if title is not None:
            review.title = title
        if content is not None:
            review.content = content
        if rating is not None:
            review.rating = rating

        session.commit()
        session.refresh(review)
        return review

    finally:
        session.close()

def delete_review(review_id):
    session = SessionLocal()
    try:
        review = session.query(Review).filter(Review.id == review_id).first()
        if not review:
            return None
        session.delete(review)
        session.commit()

        return review

    finally:
        session.close()
