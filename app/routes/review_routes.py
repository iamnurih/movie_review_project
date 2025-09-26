from flask import Blueprint, render_template, request, redirect, url_for
from app.services.review_service import (get_all_reviews, create_review, get_review_by_id, update_review, delete_review)
from datetime import datetime
from app.models import Review

review_bp = Blueprint("review", __name__, url_prefix="/review")

@review_bp.route("/")
def index():
    reviews = get_all_reviews()
    if reviews:
        avg_rating = round(sum(r.rating for r in reviews) / len(reviews), 2)
    else:
        avg_rating = 0
    return render_template("index.html", reviews=reviews, avg_rating=avg_rating)

@review_bp.route("/new", methods=["GET", "POST"])
def new_review():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        review = Review(
                  title = title,
                  content = content,
                  rating = rating,
                  created_at = datetime.now()
        )
        create_review(review)
        return redirect(url_for("review.index"))

    elif request.method == "GET":
        return render_template("new.html")

@review_bp.route("/edit/<int:review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    review = get_review_by_id(review_id)
    if not review:
        return "리뷰를 찾을 수 없습니다", 404
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        rating = int(request.form["rating"])
        update_review(review_id, title, content, rating)
        return redirect(url_for("review.index"))
    elif request.method == "GET":
        return render_template("edit.html", review=review)

@review_bp.route("/delete/<int:review_id>")
def delete_review_route(review_id):
    delete_review(review_id)
    return redirect(url_for("review.index"))