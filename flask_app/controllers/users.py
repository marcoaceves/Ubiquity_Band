from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_bcrypt import Bcrypt
from flask_app import app
import uuid as uuid
from flask_app.models.user import User

bcrypt = Bcrypt(app)


@app.route('/login')
def login():

    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register/query', methods=['POST'])
def query_registration():
    if not User.validate_user(request.form):
        return redirect(request.referrer)

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    data={
        'user_name' : request.form['user_name'],
        'email' : request.form['email'],
        'password' : pw_hash,
        'confirm_password' : request.form['confirm_password'],
    }
    User.create_user(data)
    return redirect('/login')
