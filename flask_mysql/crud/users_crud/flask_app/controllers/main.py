from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models.users import Users

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def show_all():
    users_list = Users.get_all()
    return render_template("index.html", users = users_list)

@app.route("/show_user/<int:user_id>")
def show(user_id):
    user_info = Users.get_one(user_id)
    return render_template("display_user.html", user = user_info)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/new_user/create", methods = ['POST'])
def create():
    Users.save(request.form)
    return redirect("/users")

@app.route("/user_update/<int:user_id>")
def user_update(user_id):
    user_info = Users.get_one(user_id)
    return render_template("update_user.html", user = user_info)

@app.route("/user_update/update", methods = ['POST'])
def update():
    Users.update(request.form)
    return redirect("/users")

@app.route("/user_delete/<int:user_id>")
def delete(user_id):
    Users.delete(user_id)
    return redirect("/users")