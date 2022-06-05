
from flask_app.config.mysqlconnection import connectToMySQL
import re
from flask_app import app
from datetime import datetime
import math
from flask import flash
import smtplib


db = 'ubiquity_db'

class Member:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.image = data['image']
        self.role = data['role']
        self.bio = data['bio']
        self.link = data['link']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_member(cls, data):
        query = "INSERT INTO members (first_name, last_name, image, role, bio, link) VALUES (%(first_name)s, %(last_name)s, %(image)s, %(role)s, %(bio)s, %(link)s); "
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM members WHERE id = %(id)s"
        return connectToMySQL(db).query_db(query, data)

    @classmethod
    def get_all_band_members(cls):
        query = "SELECT * FROM members;"
        results = connectToMySQL(db).query_db(query)
        members = []
        for i in results:
            members.append( cls(i) )
        print(members)
        return members
    @classmethod
    def get_one_band_member(cls, data):
        query = "SELECT * FROM members WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)
        print(results)
        return cls(results[0])

    @classmethod
    def update_member(cls,data):
        query = "UPDATE members SET first_name=%(first_name)s, last_name=%(last_name)s, image=%(image)s, role=%(role)s, bio=%(bio)s, link=%(link)s WHERE id =%(id)s "
        return connectToMySQL(db).query_db(query,data)