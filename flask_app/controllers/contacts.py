from flask import Flask, flash, request, redirect, url_for, render_template, jsonify
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app.models.image import Image
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
import json
from email.message import EmailMessage
import smtplib
@app.route('/contact')
def display_contact():

    return render_template('contact.html')

@app.route("/a", methods=['POST'])
def massage():
    data = request.form
    print(data)
    name = request.form['name']
    contact = request.form['email']
    message = request.form['message']

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('cosmicmarcobrahma@gmail.com', "pazsmajysencrhcj")
    email = EmailMessage()
    email['From'] = 'cosmicmarcobrahma@gmail.com'
    email['To'] = 'mr.aceves@gmail.com'
    email['Subject'] = 'Marco Portfolio Contact'
    email.set_content(f"{name} has a message {message} Please reply at {contact}")
    server.send_message(email)
    return jsonify ({'flash': "Thank you for contacting me, I have received your message and will respond soon."})

@app.route('/test')
def display_():
    navbar = """<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
                <div class="container px-5">
                    <a class="navbar-brand" href="/">Ubiquity</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation"><span class="navbar-toggler-icon"></span></button>
                    <div class="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
                            <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                            <li class="nav-item"><a class="nav-link" href="/band">Band</a></li>
                            <li class="nav-item"><a class="nav-link" href="/shows">Shows</a></li>
                            <li class="nav-item"><a class="nav-link" href="/music">Music</a></li>
                            <li class="nav-item"><a class="nav-link" href="/contact">Contact</a></li>
                            <!-- <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" id="navbarDropdownBlog" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Blog</a>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownBlog">
                                    <li><a class="dropdown-item" href="blog-home.html">Blog Home</a></li>
                                    <li><a class="dropdown-item" href="blog-post.html">Blog Post</a></li>
                                </ul>
                            </li> -->
                            <li class="nav-item dropdown">
                                <a class="nav-link dropdown-toggle" id="navbarDropdownPortfolio" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">Ubiquity</a>
                                <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownPortfolio">
                                    <li><a class="dropdown-item" href="/login">Admin Login</a></li>
                                    <li><a class="dropdown-item text-danger" href="/logout">Admin Logout</a></li>
                                </ul>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>"""



    return render_template('test.html', navbar=navbar)
