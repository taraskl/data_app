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
    cur = get_db().execute("SELECT * FROM data")
    rv = cur.fetchall()
    cur.close()
    print(rv)
    return render_template("index.html", cur=rv) 

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_example', None)
    if db is not None:
        db.close()    