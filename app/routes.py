from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
import os
import threading

T=threading.Thread
def pinger(ip):
    os.system('ping {}'.format(ip))
    
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        th = T(target = pinger, args = form.username.data)
        th.start()
        
        return redirect(url_for('index'))
    
    return render_template('login.html', title='Sign In', form=form)