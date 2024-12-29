from flask import Flask
from flask_pymongo import PyMongo
from app.config import Config

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    # Register Blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.track_routes import track_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(track_bp, url_prefix='/tracker')

    return app
