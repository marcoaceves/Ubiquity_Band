from flask import Flask, flash, request, redirect, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
from flask_app.models.elements import Element

from flask_app.models.logo import Logo



@app.route('/merch')

def display_merch():
    navbar = Element
    logo = Logo.get_logo()

    return render_template(
        'merch.html',navbar=navbar, logo=logo
    )


 
