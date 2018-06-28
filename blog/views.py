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

def chart():
    return render_template("chart.html")

def chart_upload():
    # print("options", options)
    return "123"

def page_404():
    return render_template("404.html")