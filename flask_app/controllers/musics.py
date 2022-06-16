from flask import Flask, flash, request, redirect, session, url_for, render_template
import os
from datetime import datetime
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.music import Music






@app.route('/music')
def display_music():
    music= Music.get_all_music()
    return render_template('music.html', music=music)

@app.route('/add/music')
def add_music():
    if 'user_id' not in session:
        return redirect('/login')


    return render_template('add_music.html')

@app.route('/add_music/query', methods=['POST'])
def query_music():
    if 'user_id' not in session:
        return redirect('/')
    data={
        'name' : request.form['name'],
        'link' : request.form['link'],
        
    }
    print("hello")
    Music.add_music(data)
    return redirect(request.referrer)


@app.route('/edit_music/query', methods=['POST'])
def query_edit_music():
    if 'user_id' not in session:
        return redirect('/')

    data = {
    'id': request.form['id']
    }

    data={
    'id' : request.form['id'],
    'name' : request.form['name'],
    'link' : request.form['link'],
    }
    Music.update_music(data)
    return redirect(request.referrer)



@app.route('/edit/music')
def edit_music():
    if 'user_id' not in session:
        return redirect('/')
    music= Music.get_all_music()

    return render_template('edit_music.html', music=music)


@app.route('/delete/music/<id>')
def delete_music(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }


    Music.delete_music(data)
    return redirect(request.referrer)