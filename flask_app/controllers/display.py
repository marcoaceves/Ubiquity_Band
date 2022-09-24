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


@app.route('/')
def display_project():

    return render_template('index.html', navbar=Element)

@app.route('/edit/index/')
def edit_index():
    logo = Logo.get_logo()

    if len(logo)<1:
        logo={"image":"default_logo.png"}
        print(logo,'y')
    print(logo, '#')
    return render_template('edit_index.html', navbar=Element, logo=logo)
