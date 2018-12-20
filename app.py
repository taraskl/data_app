from flask import Flask, render_template

import sqlite3
from flask import g

DATABASE = 'example.db'

app = Flask(__name__)

def get_db():
    db = getattr(g, '_example', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db



@app.route('/')
def hello_world():
    cur = get_db().execute("SELECT value FROM data")
    value = cur.fetchall()
    cur.close()
    list_value = [i[0] for i in value]
    print(list_value)

    data = [
    {'Date': "1", 'High': 18.79, 'Low': 17.78, 'Close': 18.37},
    {'Date': "2", 'High': 17.76, 'Low': 17.27, 'Close': 17.48},
    {'Date': "3", 'High': 18.62, 'Low': 18.05, 'Close': 18.13},
    {'Date': "June 30, 2015 00:00:05", 'High': 20.4, 'Low': 19.37, 'Close': 20.33}
    ]
    return render_template("index.html", data=data) 

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_example', None)
    if db is not None:
        db.close()    