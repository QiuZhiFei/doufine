# coding: utf-8

from flask import Flask
from flask.json import JSONEncoder
import flask_mako
from flask import make_response

import views as _v

APP_CONFIG = {
    "PROPAGATE_EXCEPTIONS": True,
    "MAKO_TRANSLATE_EXCEPTIONS": False,
    "MAKO_INPUT_ENCODING": "utf-8",
    "MAKO_OUTPUT_ENCODING": "utf-8",
    "MAKO_DEFAULT_FILTERS": ["decode.utf8"],
}

app = Flask(__name__)
app.config.update(APP_CONFIG)
app.json_decoder = JSONEncoder

app.add_url_rule("/", view_func=_v.index)
app.add_url_rule("/user", view_func=_v.show_user_profile)
app.add_url_rule("/chart", view_func=_v.chart)
app.add_url_rule("/404", view_func=_v.page_404)
app.add_url_rule("/chart_upload", view_func=_v.chart_upload)
app.add_url_rule("/user/moments", view_func=_v.show_user_moments)
app.add_url_rule("/slack", view_func=_v.handle_slack, methods=['GET', 'POST'])

# app.static_folder = "./static/"
app.static_url_path = "./static/"
app.template_folder = "./templates/"
flask_mako.MakoTemplates(app)

app.debug = True


if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 5000,
    )




# def create_app():
#     app = Flask(__name__)
#     app.config.update(APP_CONFIG)
#     app.json_decoder = JSONEncoder

#     app.add_url_rule("/", view_func=_v.index)
#     app.add_url_rule("/user", view_func=_v.show_user_profile)
#     app.add_url_rule("/chart", view_func=_v.chart)
#     app.add_url_rule("/404", view_func=_v.page_404)
#     app.add_url_rule("/chart_upload", view_func=_v.chart_upload)
#     app.add_url_rule("/user/moments", view_func=_v.show_user_moments)
#     app.add_url_rule("/slack", view_func=_v.handle_slack, methods=['GET', 'POST'])

#     # app.static_folder = "./static/"
#     app.static_url_path = "./static/"
#     app.template_folder = "./templates/"
#     flask_mako.MakoTemplates(app)

#     app.debug = True
#     app.run(
#          host = "0.0.0.0",
#          port = 5000,
#     )

#     return app




# @app.route('/')
# def index():
#     return '123'

# @app.route('/user/<username>')
# def show_user_profile(username):
#     return 'user %s' % username


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return 'login'


# @app.route('/user/moments')
# def show_user_moments():
#     return "123"
    # response = make_response(jsonify(response=get_articles(ARTICLES_NAME)))
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # response.headers['Access-Control-Allow-Methods'] = 'GET'
    # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type' 

    # return _v.show_user_moments();


# if __name__ == '__main__':
#     create_app()