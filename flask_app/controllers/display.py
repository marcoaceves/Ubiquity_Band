
from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
from flask_app.models.elements import Element
from flask_app.models.logo import Logo
from flask_app.models.index import Videos

from flask_app.models.logo import logo

@app.route('/')
def display_project():
    logo = Logo.get_logo()

    if len(logo)<1:
        logo={"image":"default_logo.png"}
    

    return render_template('index.html', navbar=Element, logo=logo)

@app.route('/edit/index/')
def edit_index():
    video_one=Videos.get_videos()['video_one']
    video_two=Videos.get_videos()['video_two']

    return render_template('edit_index.html', navbar=Element, logo=logo, video_one=video_one, video_two=video_two)
    
@app.route('/edit_video1/query', methods=['POST'])
def edit_video_one():

    video_two= Videos.get_videos()
    print('Videos', video_two)

    data={
        'video_one' : request.form['video_one'],
        'video_two' : video_two["video_two"]
        
    }
    Videos.delete_videos()
    Videos.add_video(data)

    return redirect(request.referrer)

@app.route('/edit_video2/query', methods=['POST'])
def edit_video_two():

    video_two= Videos.get_videos()
    print('Videos', video_two)

    data={
        'video_one' : video_two["video_one"],
        'video_two' : request.form['video_two']
        
    }
    Videos.delete_videos()
    Videos.add_video(data)

    return redirect(request.referrer)
