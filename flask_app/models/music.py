from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash 

db = 'ubiquity_db'

class Music:
    def __init__(self, data):
        self.id= data['id']
        self.name= data['name']
        self.link= data['link']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def add_music(cls,data):
        query="INSERT INTO music (name,link) VALUES (%(name)s,%(link)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_music(cls):
        query = "SELECT * FROM music;"
        results = connectToMySQL(db).query_db(query)
        # if results == False:
        #     no_shows =[{"title":"There is no shows!"}]
        #     return(no_shows)

        music = []
        for i in results:
            music.append( cls(i) )
        print(music)
        return music

    @classmethod
    def delete_music(cls, data):
        query = "DELETE FROM music WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_one_music(cls, data):
        query = "SELECT * FROM shows WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def update_music(cls,data):
        query = "UPDATE shows SET name=%(name)s,  link=%(link)s WHERE id =%(id)s "
        return connectToMySQL(db).query_db(query,data)