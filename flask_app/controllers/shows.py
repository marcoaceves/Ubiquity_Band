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
from flask_app.models.show import Show



# image proccessing
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'avif'])
UPLOAD_FOLDER = 'flask_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1080 * 1554
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# -----------------------------------------------------------------
@app.route('/add/show')
def add_show_form():
    if 'user_id' not in session:
        return redirect('/login')
    data={'id':session["user_id"]}
    user=User.get_user(data)

    return render_template('add_show.html', user=user)



@app.route('/shows')
def display_shows():
    shows= Show.get_all_shows()


    return render_template('shows.html', shows=shows)



@app.route('/add_show/query', methods=['POST'])
def query_show():
    files = request.files.getlist('files[]')
    print(files)
    pic_name=''
    for file in files:
        print("hello")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pic_name = str(uuid.uuid1()) + "_" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
    print(pic_name,'pic_name')
    data={
        'title' : request.form['title'],
        'show_date' : request.form['show_date'],
        'link' : request.form['link'],
        'image' : pic_name,
    }
    print("hello")
    Show.add_show(data)
    return redirect(request.referrer)