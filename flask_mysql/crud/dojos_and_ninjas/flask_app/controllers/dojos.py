from flask import render_template, request, redirect, session, url_for
from flask_app import app
from flask_app.models import dojo
from flask_app.models import ninja

@app.route("/")
def index():
    return redirect("/dojos")

@app.route("/dojos")
def main():
    dojo_list = dojo.Dojo.get_all()
    return render_template("dojos.html", dojos = dojo_list)

@app.route("/dojos/<int:dojo_id>")
def dojo_show(dojo_id):
    data={"id":dojo_id}
    dojo_info = dojo.Dojo.get_group(data)
    return render_template("dojo_show.html", dojo = dojo_info)

@app.route("/new_dojo", methods = ["POST"])
def add_dojo():
    dojo.Dojo.save(request.form)
    return redirect("/")
