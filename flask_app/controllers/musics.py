from flask import Flask, flash, request, redirect, session, url_for, render_template
import os
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_app import app







@app.route('/music')
def display_music():

    return render_template('music.html')

@app.route('/add/music')
def add_music():

    return render_template('add_music.html')
