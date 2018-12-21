from flask import Flask, render_template
from flask import g
import sqlite3
import codecs
import csv


DATABASE = 'data.sqlite3.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_data.sqlite3', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def twst():
    cur = get_db().execute("SELECT value FROM data")
    value = cur.fetchall()
    cur.close()
    list_of_value = [i[0] for i in value]
    # remove not float value from list
    for i in list_of_value:
        if type(i) is not float:
            list_of_value.remove(i)

    max_list_value = (max(list_of_value))
    int_max_list_value = int(max_list_value)+2

    # make a dictionary with data
    data=[]
    maxcounter = 0
    for i in range(int_max_list_value):
        counter = 0
        for value in list_of_value:
            if value >=i and value <i+1:
                counter +=1
    # print("counter", counter)
        d={'x':'','y':''}
        d['x'] = i
        d['y'] = counter
        data.append(d)
    # find a maxcounte
        if counter > maxcounter:
            maxcounter = counter   
        
    return render_template("test.html", data=data, xrange=int_max_list_value, yrange=maxcounter) 

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_example', None)
    if db is not None:
        db.close()    