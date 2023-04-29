from flask import render_template, request, redirect, session, url_for
from flask_app import app

@app.route("/")
def index():
    if "visited" in session:
        session["count"] += 1
    else:
        session["visited"] = "yes"
        session["count"] = 1

    return render_template("index.html", color1 = "white")

@app.route("/destroy_session")
def session_clear():
    session.clear()
    return redirect(url_for("index"))

@app.route("/two_visits")
def two_visits():
    session["count"] += 1
    return redirect(url_for("index"))

@app.route("/mult_visit", methods = ["GET", "POST"])
def mult_visit():
    session["count"] += int(request.form["mult_visit"])-1
    return redirect(url_for("index"))