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



@app.route('/add/member')
def add_band_member_form():
    if 'user_id' not in session:
        return redirect('/login')
    data={'id':session["user_id"]}
    user=User.get_user(data)

    return render_template('band_member_form.html', user=user)

