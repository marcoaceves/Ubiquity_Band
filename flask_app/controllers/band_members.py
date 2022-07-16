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
from flask_app.models.band_member import Member
from flask_app.models.elements import Element
bcrypt = Bcrypt(app)


# image proccessing
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'avif'])
UPLOAD_FOLDER = 'flask_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1080 * 1554
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# -----------------------------------------------------------------


@app.route('/add/member')
def add_band_member_form():
    if 'user_id' not in session:
        return redirect('/login')
    data={'id':session["user_id"]}
    user=User.get_user(data)

    return render_template('band_member_form.html', user=user, navbar=Element)



@app.route('/band')
def display_band():
    members= Member.get_all_band_members()
    print(members[0].image)

    return render_template('band.html', members=members, navbar=Element)



@app.route('/add_member/query', methods=['POST'])
def query_band_member():
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
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'role' : request.form['role'],
        'bio' : request.form['bio'],
        'link' : request.form['link'],
        'image' : pic_name,
    }
    print("hello")
    Member.add_member(data)
    return redirect(request.referrer)


@app.route('/edit_member/query', methods=['POST'])
def query_edit_member():

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
            img = Member.get_one_band_member(data)
            pic_name = img.image
            print(pic_name, "^^^^^")
            data={
            'id' : request.form['id'],
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'role' : request.form['role'],
            'bio' : request.form['bio'],
            'link' : request.form['link'],
            'image' : pic_name,
            }
            Member.update_member(data)
            return redirect(request.referrer)
        else:
            data = {
            'id': request.form['id']
            }
            img = Member.get_one_band_member(data)
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
                'first_name' : request.form['first_name'],
                'id' : request.form['id'],
                'last_name' : request.form['last_name'],
                'role' : request.form['role'],
                'bio' : request.form['bio'],
                'link' : request.form['link'],
                'image' : pic_name,
            }
            Member.update_member(data)
            return redirect(request.referrer)


@app.route('/edit/band')
def edit_band():
    if 'user_id' not in session:
        return redirect('/')
    members= Member.get_all_band_members()
    print(members[0].image)

    return render_template('edit_band_member.html', members=members, navbar=Element)

@app.route('/delete/member/<id>')
def delete_member(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    img = Member.get_one_band_member(data)
    image = img.image
    print(image)

    os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], image))

    Member.delete(data)
    return redirect(request.referrer)


