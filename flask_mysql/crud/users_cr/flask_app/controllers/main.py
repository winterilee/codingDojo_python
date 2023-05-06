from flask import render_template, request, redirect, session, url_for
from flask_app import app
from users import Users

@app.route("/")
def index():
    users_list = Users.get_all()
    return render_template("index.html", users = users_list)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/new_user/create", methods = ['POST'])
def create():
    Users.save(request.form)
    return redirect("/")