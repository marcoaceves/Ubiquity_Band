from flask import Flask, flash, request, redirect, session, url_for, render_template
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
def login_html():
    if 'user_id' in session:
        return redirect('/dashboard')

    return render_template('login.html')

@app.route('/register/hfjksahfjhsa5064506456/fsa70475fs')
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


@app.route('/login/query', methods=['POST'])
def login():
    data={'email' : request.form['email']}
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid Email or Password!', 'login')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid Email or Password!', 'login')
        return redirect('/login')
    session['user_id']  = user_in_db.id

    return redirect ('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/login')
    data={'id':session["user_id"]}
    user=User.get_user(data)
    return render_template('dashboard.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
