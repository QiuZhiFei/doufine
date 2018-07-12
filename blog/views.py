# coding: utf-8
 
import flask
from flask_mako import render_template
from flask import jsonify
from flask import make_response, request
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
    page = request.args.get("p", "1")
    data = weibo.fetchZhifeiData(int(page)).get("data", {})
    cards = data.get("cards", [])

    # return jsonify(cards)

    items = []
    for card in cards:
        mblog = card.get('mblog', {})
        titles = re.compile("\#(.*?)\#", re.S).findall(mblog.get('text', ''))
        texts = re.compile("(.*?)<br", re.S).findall(mblog.get('text', ''))

        if len(titles) == 0 or len(texts) == 0:
            continue

        item = {}
        item['title'] = titles[0]
        item['text'] = texts[0]
        
        item['original_pic'] = mblog.get('original_pic', '')
        item['created_at'] = mblog.get('created_at', '')
        item['scheme'] = card.get('scheme', '')
        
        items.append(item)

    # return jsonify(items)

    result = {"items": items}

    response = make_response(jsonify(result))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 

    return response

def page_404():
    return render_template("404.html")


def handle_slack():
    print("request == ", request)
    return "123"