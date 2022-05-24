from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid



@app.route('/login',methods=["POST","GET"])
def login():

    return render_template('login.html', images=Image.get_all_images())

@app.route('/register',methods=["POST","GET"])
def register():

    return render_template('register.html', images=Image.get_all_images())