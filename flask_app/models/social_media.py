from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash 

db = 'ubiquity_db'

class Social_media:
    def __init__(self, data):
        self.id= data['id']
        self.name= data['name']
        self.link= data['link']



    @classmethod
    def update_link(cls,data):
        query="UPDATE social_media_links SET link = %(link)s where id = %(id)s;" 
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_links(cls):
        query = "SELECT * FROM social_media_links;"
        results = connectToMySQL(db).query_db(query)

        links = []
        for i in results:
            links.append( cls(i) )
        print(links)
        return links
