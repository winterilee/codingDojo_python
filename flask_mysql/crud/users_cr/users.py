from mysqlconnection import connectToMySQL

class Users:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL("users_schema").query_db(query)
        user_list = []
        for i in results:
            user_list.append(cls(i))
        return user_list
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(fname)s, %(lname)s, %(em)s);"
        result = connectToMySQL("users_schema").query_db(query, data)
        return result
