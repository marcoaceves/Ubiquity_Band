from flask import Flask, flash, request, redirect, session, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
from flask_app.models.show import Show

from flask_app.models.elements import Element
from flask_app.models.logo import Logo
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

    return render_template('add_show.html', user=user, navbar=Element)



@app.route('/shows')
def display_shows():
    shows= Show.get_all_shows()
    logo = Logo.get_logo()
    return render_template('shows.html', shows=shows, navbar=Element, logo=logo)



@app.route('/add_show/query', methods=['POST'])
def query_show():
    if 'user_id' not in session:
        return redirect('/')
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



@app.route('/edit_show/query', methods=['POST'])
def query_edit_show():
    if 'user_id' not in session:
        return redirect('/')
    files = request.files.getlist('files[]')
    for file in files:
        file=secure_filename(file.filename)
        print(file, '$$$$$$$$$$$')

        if len(file)<1:
            print("Files are Empty")
            data = {
            'id': request.form['id']
            }
            img = Show.get_one_show(data)
            pic_name = img.image
            print(pic_name, "^^^^^")
            data={
            'id' : request.form['id'],
            'title' : request.form['title'],
            'show_date' : request.form['show_date'],
            'link' : request.form['link'],
            'image' : pic_name,
            }
            Show.update_show(data)
            return redirect(request.referrer)
        else:
            data = {
            'id': request.form['id']
            }
            img = Show.get_one_show(data)
            image = img.image
            os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], image))
            files = request.files.getlist('files[]')
            pic_name=''
            for file in files:
                if file and allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    pic_name = str(uuid.uuid1()) + "_" + filename
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
            print(pic_name,'pic_name')
            data={
                'title' : request.form['title'],
                'id' : request.form['id'],
                'show_date' : request.form['show_date'],
                'link' : request.form['link'],
                'image' : pic_name,
            }
            Show.update_show(data)
            return redirect(request.referrer)


@app.route('/edit/shows')
def edit_shows():
    if 'user_id' not in session:
        return redirect('/')
    shows= Show.get_all_shows()
    print(shows[0].image)

    return render_template('edit_shows.html', shows=shows, navbar=Element)

@app.route('/delete/show/<id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    img = Show.get_one_show(data)
    image = img.image
    print(image)

    os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], image))

    Show.delete_show(data)
    return redirect(request.referrer)
