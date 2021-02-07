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


@app.route('/score')
def score():
    con = sqlite3.connect('movie250.db')
    cus = con.cursor()
    datas = cus.execute("select rate,count(rate) from movie group by rate;")
    score_list = []
    group_list = []
    for data in datas:
        score_list.append(data[0])
        group_list.append(data[1])
    return render_template('score.html', score_list=score_list, group_list=group_list)


if __name__ == '__main__':
    app.debug = True
    app.run()
