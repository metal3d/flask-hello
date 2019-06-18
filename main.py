import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/')
def index():
    return "Hello !!"


@app.route('/greeting/<user>')
def greeting(user):
    return "Hello dear %s" % user


@app.route('/echo', methods=['POST'])
def echo():
    if 'name' not in request.json:
        return "Please set name in json request", 500

    return """
    You gave {name} as "name" value
    """.format(**request.json)
