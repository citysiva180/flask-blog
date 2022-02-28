# Initialization code
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "xEncryPtWorker11"

    @app.route("/")
    def home():
        return "<h1>Home Page</h1>"

    @app.route("/profile")
    def profile():
        return "<h1>Profile Page</h1>"

    return app
