from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    db = "dojos_and_ninjas_schema"
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL(cls.db).query_db(query)
        dojo_list = []
        for i in results:
            dojo_list.append(cls(i))
        return dojo_list
    
    @classmethod
    def get_one(cls, dojo_id):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        data = {"id":dojo_id}
        result = connectToMySQL(cls.db).query_db(query, data)
        return cls(result[0])
    
    @classmethod
    def get_group(cls, data):
        query = "SELECT * FROM dojos JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        selected_dojo = cls(results[0])
        for row in results:
            ninja_list = {
                "id":row["ninjas.id"],
                "first_name":row["first_name"],
                "last_name":row["last_name"],
                "age":row["age"],
                "created_at":row["ninjas.created_at"],
                "updated_at":row["ninjas.updated_at"],
                "dojo_id":row["dojo_id"]
            }
            selected_dojo.ninjas.append(ninja.Ninja(ninja_list))
        return selected_dojo
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        result = connectToMySQL(cls.db).query_db(query, data)
        return result