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

@app.route("/update_ninja/<int:ninja_id>")
def update_form(ninja_id):
    ninja_info = ninja.Ninja.get_one(ninja_id)
    return render_template("update_ninja.html", ninja = ninja_info)

@app.route("/update_ninja/submit", methods = ["POST"])
def update_ninja():
    ninja.Ninja.update(request.form)
    return redirect(f"/dojos/{request.form['dojo_id']}")

@app.route("/delete_ninja/<int:ninja_id>/<int:dojo_id>")
def delete_ninja(ninja_id, dojo_id):
    ninja.Ninja.delete(ninja_id)
    return redirect("/dojos/" + str(dojo_id))