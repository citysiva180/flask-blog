# Initialization code
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "xEncryPtWorker11"

    from .views import views
    from .auth import auth
    # registering blue print
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app
