from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash 

db = 'ubiquity_db'

class Show:
    def __init__(self, data):
        self.id= data['id']
        self.title= data['title']
        self.show_date= data['show_date']
        self.image= data['image']
        self.link= data['link']
        self.created_at= data['created_at']
        self.updated_at= data['updated_at']

    @classmethod
    def add_show(cls,data):
        query="INSERT INTO shows (title, show_date, image, link) VALUES (%(title)s,%(show_date)s,%(image)s, %(link)s);"
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_all_shows(cls):
        query = "SELECT * FROM shows;"
        results = connectToMySQL(db).query_db(query)
        # if results == False:
        #     no_shows =[{"title":"There is no shows!"}] 
        #     return(no_shows)

        shows = []
        for i in results:
            shows.append( cls(i) )
        print(shows)
        return shows