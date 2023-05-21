from flask import render_template, request, redirect, flash, session, url_for
from flask_app import app
from flask_app.models import recipe

@app.route("/dashboard")
def dashboard():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    all_recipes = recipe.Recipe.get_all()
    return render_template("dashboard.html", recipes = all_recipes)

@app.route("/new_recipe")
def new_recipe():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    return render_template("new_recipe.html")

@app.route("/create_recipe", methods = ["POST"])
def create_recipe():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(url_for("new_recipe"))
    else:
        recipe.Recipe.create_recipe(request.form)
    return redirect(url_for("dashboard"))
