from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import user

@app.route("/")
def index():
    return redirect("/users")

@app.route("/users")
def show_all():
    users_list = user.User.get_all()
    return render_template("index.html", users = users_list)

@app.route("/show_user/<int:user_id>")
def show(user_id):
    user_info = user.User.get_one(user_id)
    return render_template("display_user.html", user = user_info)

@app.route("/new_user")
def new_user():
    return render_template("new_user.html")

@app.route("/new_user/create", methods = ['POST'])
def create():
    if not user.User.validate_user(request.form):
        return redirect("/new_user")
    user.User.save(request.form)
    return redirect("/")

@app.route("/user_update/<int:user_id>")
def update_form(user_id):
    user_info = user.User.get_one(user_id)
    return render_template("update_user.html", user = user_info)

@app.route("/user_update/submit", methods = ['POST'])
def update():
    if not user.User.validate_user(request.form):
        return redirect(f"/user_update/{request.form['id']}")
    user.User.update(request.form)
    return redirect("/")

@app.route("/user_delete/<int:user_id>")
def delete(user_id):
    user.User.delete(user_id)
    return redirect("/")