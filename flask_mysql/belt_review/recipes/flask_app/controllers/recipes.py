from flask import render_template, request, redirect, flash, session, url_for
from flask_app import app
from flask_app.models import recipe, user

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
        data = {
            "name": request.form["name"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "date": request.form["date"],
            "under": int(request.form["under"]),
            "user_id": session["logged_in_id"]
        }
        recipe.Recipe.create_recipe(data)
    return redirect(url_for("dashboard"))

@app.route("/view_recipe/<int:recipe_id>")
def view_recipe(recipe_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    recipe_info = recipe.Recipe.get_one(recipe_id)
    return render_template("view_recipe.html", recipe = recipe_info)

@app.route("/edit_recipe/<int:recipe_id>")
def edit_recipe(recipe_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    recipe_info = recipe.Recipe.get_one(recipe_id)
    return render_template("edit_recipe.html", recipe = recipe_info)
    

@app.route("/update_recipe", methods = ["POST"])
def update_recipe():
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    if not recipe.Recipe.validate_recipe(request.form):
        return redirect(f"/edit_recipe/{int(request.form['id'])}")
    else:
        data = {
            "id": request.form["id"],
            "name": request.form["name"],
            "description": request.form["description"],
            "instruction": request.form["instruction"],
            "date": request.form["date"],
            "under": int(request.form["under"])
        }
        recipe.Recipe.update_recipe(data)
    return redirect(url_for("dashboard"))

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    if "logged_in_id" not in session:
        return redirect(url_for("index"))
    recipe.Recipe.delete_recipe(recipe_id)
    return redirect(url_for("dashboard"))
