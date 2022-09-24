from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash 

db = 'ubiquity_db'

class Logo:
    def __init__(self, data):
        self.id= data['id']
        self.image= data['image']

    @classmethod
    def add_logo(cls,data):
        query="INSERT INTO logo (image) VALUES (%(image)s);"
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_logo(cls):
        query = "SELECT * FROM logo;"
        results = connectToMySQL(db).query_db(query)
        print(results, '*')
        if len(results) < 1:
             no_logo =[] 
             return(no_logo)

        logo = results[0]
        print(logo,'hello')
        return logo
    @classmethod
    def delete_logo(cls):
        query = "TRUNCATE TABLE  logo;"
        return connectToMySQL(db).query_db(query)
