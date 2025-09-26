from flask import Flask
from .routes.review_routes import review_bp
from .config import Config, engine, SessionLocal
from .models import Basegit

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        Base.metadata.create_all(bind=engine)

    app.session = SessionLocal
    app.register_blueprint(review_bp)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        SessionLocal.remove()

    return app
