from flask import Blueprint, render_template
auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return "Login"


@auth.route("/register")
def register():
    return "register"


@auth.route("/logout")
def logout():
    return "logout"
