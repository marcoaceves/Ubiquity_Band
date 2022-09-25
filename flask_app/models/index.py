from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app 
from flask import flash 

db = 'ubiquity_db'

class Videos:
    def __init__(self, data):
        self.id= data['id']
        self.video_one= data['video_one']
        self.video_two= data['video_two']

    @classmethod
    def add_video(cls,data):
        query="INSERT INTO videos (video_one, video_two) VALUES (%(video_one)s, %(video_two)s);"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def add_video_two(cls,data):
        query="INSERT INTO logo (image) VALUES (%(image)s);"
        return connectToMySQL(db).query_db(query, data)
    @classmethod
    def get_videos(cls):
        query = "SELECT * FROM videos;"
        results = connectToMySQL(db).query_db(query)
        print(results, '*')
        if len(results) < 1:
             no_logo =[] 
             return(no_logo)

        videos = results[0]
        print(videos,'hello')
        return videos
        
    @classmethod
    def delete_videos(cls):
        query = "TRUNCATE TABLE  videos;"
        return connectToMySQL(db).query_db(query)


