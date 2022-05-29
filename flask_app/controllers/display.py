from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid
from flask_app.models.user import User



@app.route('/')
def display_project():

    return render_template('index.html', images=Image.get_all_images())

@app.route('/music')
def display_music():

    return render_template('music.html', images=Image.get_all_images())

@app.route('/band')
def display_band():


    return render_template('band.html', images=Image.get_all_images())