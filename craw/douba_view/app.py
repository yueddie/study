# -*- coding: utf-8 -*-
from flask import Flask, render_template
import sqlite3


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/index')
def index():
    return hello_world()


@app.route('/movies')
def movies():
    con = sqlite3.connect('movie250.db')
    cus = con.cursor()
    datas = cus.execute("select * from movie;")
    datalist = []
    for data in datas:
        datalist.append(data)
    return render_template('movies.html', datalist=datalist)


if __name__ == '__main__':
    print(__package__)
    # app.debug = True
    # app.run()
