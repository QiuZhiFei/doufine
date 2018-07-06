# coding: utf-8
 
import flask
from flask_mako import render_template
from flask import jsonify
import re

import sys
sys.path.append('weibo.py')

import weibo

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

def show_user_moments():
    data = weibo.fetchZhifeiData(1).get("data", {})
    cards = data.get("cards", [])

    items = []
    for card in cards:
        mblog = card.get('mblog', {})

        text = mblog.get('text', '')



        # r = re.compile("(.*?)<br", re.S)
        # te = r.findall(text)[0]


        r = re.compile("\#(.*?)\#", re.S)
        te = r.findall(text)

        # return te


        

        # 

        item = {}
        item['title'] = re.compile("(.*?)<br", re.S).findall(mblog.get('text', ''))[0]
        item['text'] = re.compile("\#(.*?)\#", re.S).findall(mblog.get('text', ''))[0]
        item['original_pic'] = mblog.get('original_pic', '')
        items.append(item)

    # print("data == ", data);
    # data = {"name": "zhifei"}
    return jsonify(items)

def page_404():
    return render_template("404.html")