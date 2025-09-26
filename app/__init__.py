from flask import Flask
from app.routes.review_routes import review_bp
from app.config import config, engine, SessionLocal
from app.models import Base

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        Base.metadata.create_all(bind=engine)

    app.session = SessionLocal
    app.register_blueprint(review_bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app