from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Recipe:
    db = "recipes_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instruction = data["instruction"]
        self.under = data["under"]
        self.date = data["date"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
    
    @classmethod
    def create_recipe(cls, data):
        query = "INSER INTO recipes (name, description, instruction, under, date, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(under)s, %(date)s, %(user_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes JOIN users ON recipes.user_id = users.id;"
        results = connectToMySQL(cls.db).query_db(query)
        recipe_list = []
        for row in results:
            one_recipe = {
                "id": row["recipes.id"],
                "name": row["name"],
                "under": row["under"],
                "username": row["first_name"],
                "user_id": row["users.id"]
            }
            recipe_list.append(one_recipe)
        return recipe_list
    
    @staticmethod
    def validate_recipe(recipe):
        is_valid = True
        if len(recipe["name"]) <= 0:
            flash("Name is required.", "recipe")
            is_valid = False
        elif len(recipe["name"]) < 3:
            flash("Name must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe["description"]) <= 0:
            flash("Description is required.", "recipe")
            is_valid = False
        elif len(recipe["description"]) < 3:
            flash("Description must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe["instruction"]) <= 0:
            flash("Instruction is required.", "recipe")
            is_valid = False
        elif len(recipe["instruction"]) < 3:
            flash("Instruction must be at least 3 characters.", "recipe")
            is_valid = False
        if len(recipe["date"]) <= 0:
            flash("Date is required.", "recipe")
            is_valid = False
        if len(recipe["under"]) <= 0:
            flash("Please check whether the dish takes under 30 minutes or not.", "recipe")
            is_valid = False
        return is_valid