from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import dojo
from flask_app.models import ninja

@app.route("/new_ninja")
def new_ninja():
    dojo_list = dojo.Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojo_list)

@app.route("/new_ninja/add", methods = ["POST"])
def add_ninja():
    ninja.Ninja.save(request.form)
    return redirect("/")