from flask import render_template, request, redirect, flash, session, url_for
from flask_app import app
from flask_app.models import user
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_user", methods = ["POST"])
def create():
    if not user.User.validate_user(request.form):
        return redirect(url_for("index"))
    else:
        data = {
            "first_name": request.form["first_name"],
            "last_name": request.form["last_name"],
            "email": request.form["email"],
            "password": bcrypt.generate_password_hash(request.form["password"])
        }
        user.User.save(data)
        return redirect (url_for("index"))

@app.route("/login", methods = ["POST"])
def login():
    data = {"email": request.form["email"]}
    user_in_db = user.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid login.")
        return redirect(url_for("index"))
    if not bcrypt.check_password_hash(user_in_db.password, request.form["password"]):
        flash("Invalid login.")
        return redirect(url_for("index"))
    session["user_id"] = user_in_db.id
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
