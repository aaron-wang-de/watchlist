# Author:Aaron
# -*- coding = utf-8 -*-
# @Time: 10/4/20 2:41 AM
# @Author: aaron
# @Site: 
# @File: app.py
# @Software: PyCharm

from flask import Flask
from flask import url_for
app = Flask(__name__)


@app.route('/home')
def home():
    return 'welcome'


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/')
def beauty():
    return '<h1>Hello Totoro!</h1><img src="https://www.timessouth.com/wp-content/gallery/hot-beauty-neha-sharma/Neha-Sharma-1.jpg">'


@app.route('/user/<name>')
def user_page(name):
    return "{}'s page".format(name)


@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('test_url_for', num=2))
    return url_for('hello')


if __name__ == '__main__':
    app.run(debug=True)