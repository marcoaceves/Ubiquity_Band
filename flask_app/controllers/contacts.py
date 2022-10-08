from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
from flask_app.models.elements import Element
import json
from email.message import EmailMessage
import smtplib
@app.route('/contact')
def display_contact():
    navbar = Element
    return render_template('contact.html', navbar=navbar)

@app.route("/a", methods=['POST'])
def massage():
    data = request.form
    print(data, "hello")
    name = request.form['name']
    contact = request.form['email']
    message = request.form['message']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('ubiquityofficialwebsite@gmail.com', " ")
    email = EmailMessage()
    email['From'] = 'ubiquityofficialwebsite@gmail.com'
    email['To'] = 'ubiquityofficial@gmail.com'
    email['Subject'] = 'Ubiquity Official Website'
    email.set_content(f"{name} wants to get in touch. Message: {message}. Please reply at {contact}")
    server.send_message(email)
    return jsonify ({'flash': "We have received your message and will respond soon."})

@app.route('/test')
def display_():

    navbar = Element


    return render_template('test.html', navbar=navbar)
