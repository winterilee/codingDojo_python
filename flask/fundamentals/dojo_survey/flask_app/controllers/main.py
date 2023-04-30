from flask import render_template, request, redirect, session, url_for
from flask_app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/process", methods = ["GET", "POST"])
def process():
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["language"] = request.form["language"]
    session["comments"] = request.form["comments"]
    return redirect(url_for("result"))

@app.route("/result")
def result():
    return render_template("result.html")

@app.route("/go_back")
def go_back():
    return redirect(url_for("index"))