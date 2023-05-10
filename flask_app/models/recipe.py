from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import app
from flask_app.models.user import User

class Recipe:
    db = "recipes_schema"
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 = data['under_30']
        self.made = data['made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        

    @classmethod
    def save(cls, data):
        query = """
            INSERT INTO recipes(name,description,instructions,under_30, made, user_id)
            VALUES (%(name)s,%(description)s,%(instructions)s,%(under_30)s,%(made)s,%(user_id)s)
        """
        return connectToMySQL(cls.db).query_db(query, data)
        
    @classmethod
    def select_one(cls, data):
        query="""SELECT * FROM recipes 
            JOIN users ON users.id = recipes.user_id 
            WHERE recipes.id=%(id)s"""
        result=connectToMySQL(cls.db).query_db(query, data)
        return result[0]
            
    # C
    @classmethod
    def insert(cls, data):
        query="INSERT INTO recipes(name, description, instructions, under_30, creator_id) VALUES(%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(creator_id)s)"
        return connectToMySQL(cls.db).query_db(query, data)

    # READ

    # U
    @classmethod
    def update(cls,data):
        query="UPDATE recipes SET name=%(name)s, description=%(description)s, instructions=%(instructions)s, under_30=%(under_thirty)s, creator_id=%(creator_id)s WHERE id = %(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
        
    # D
    @classmethod
    def delete(cls,data):
        query="DELETE FROM recipes WHERE id=%(id)s"
        return connectToMySQL(cls.db).query_db(query, data)
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM recipes;"
        results = connectToMySQL(cls.db).query_db(query)
        print (results)
        recipes = []
        for row in results:
            recipes.append(cls(row))
        return recipes
# change receipes to movies

    @staticmethod 
    def validate(data):
        is_valid = True
        if len(data['name']) < 2:
            flash("Name Please")
            is_valid = False
        if len(data['description']) < 2:
            flash("Tell Me, your secrets")
            is_valid = False
        if len(data['instructions']) < 10:
            flash("Tell Us, How it's made!!")
            is_valid = False
        if "under_30" not in data:
            flash("Date is needed!!")
            is_valid = False
        return is_valid