from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user")
def create():
    if not user.User.validate_user(request.form):
        return redirect("/")
    user.User.save(request.form)
    return redirect ("/")