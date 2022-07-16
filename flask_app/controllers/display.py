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


@app.route('/')
def display_project():

    return render_template('index.html', navbar=Element)

