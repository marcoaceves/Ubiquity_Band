from flask import Flask, flash, request, redirect, session, url_for, render_template
import os
from werkzeug.utils import secure_filename
import urllib.request
from datetime import datetime
from flask_app import app
import uuid as uuid
from flask_app.models.user import User
from flask_app.models.logo import Logo

from flask_app.models.elements import Element

# image proccessing
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif', 'avif'])
UPLOAD_FOLDER = 'flask_app/static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1080 * 1554
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
# -----------------------------------------------------------------


@app.route('/add_logo/query', methods=['POST'])
def query_logo():


    if 'user_id' not in session:
        return redirect('/')
    # delete proccess
    
    img = Logo.get_logo()
    if len(img)>1:
        image = img['image']
        print(image, "image")
        Logo.delete_logo()

        try:
            os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], image))
        except Exception:
            pass

    files = request.files.getlist('files[]')
    print(files)
    pic_name=''
    for file in files:

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            pic_name = str(uuid.uuid1()) + "_" + filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], pic_name))
    print(pic_name,'pic_name')
    data={
        'image' : pic_name,
    }

    Logo.add_logo(data)
    return redirect(request.referrer)

# @app.route('/delete/show/<id>')
# def delete_show(id):
#     if 'user_id' not in session:
#         return redirect('/')
#     data = {
#         'id': id
#     }
#     img = Show.get_one_show(data)
#     image = img.image
#     print(image)

#     os.unlink(os.path.join(app.config['UPLOAD_FOLDER'], image))

#     Show.delete_show(data)
#     return redirect(request.referrer)
