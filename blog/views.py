# coding: utf-8
 
import flask
from flask_mako import render_template

def index():
    return render_template("index.html")


def login():
    return 'login'


def show_user_profile():
    args = flask.request.args
    id = args.get('id', '')
    print(id)
    return 'user %s' % id