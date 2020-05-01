import sqlite3
from datetime import datetime
from flask import Flask, jsonify, render_template, request
import json


conn = sqlite3.connect('login_activity.db')

c = conn.cursor()
table_setup_query = '''CREATE TABLE IF NOT EXISTS details (id integer primary key autoincrement, ip text, login timestamp, logout timestamp, duration number)'''
c.execute(table_setup_query)

app = Flask(__name__)

@app.route("/" , methods = ["GET" , "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":

        global c

        table_setup_query = '''CREATE TABLE IF NOT EXISTS details (id integer primary key autoincrement, ip text, login timestamp, logout timestamp, duration number)'''
        c.execute(table_setup_query)

        db = [ list(row) for row in c.execute(f"select * from details order by login desc") ]

        db = [{
                "id" : doc[0],
                "ip" : doc[1],
                "login" : doc[2],
                "logout" : doc[3],
                "duration" : doc[4]
        } for doc in db ]

        print(db)

        return jsonify(db)

@app.route("/login")
def login():
    ip = request.remote_addr

    # junk

    global c

    table_setup_query = '''CREATE TABLE IF NOT EXISTS details (id integer primary key autoincrement, ip text, login timestamp, logout timestamp, duration number)'''
    c.execute(table_setup_query)

    insert_query = f"INSERT INTO details(ip,login) VALUES ('{ip}',datetime('now'))"
    c.execute(insert_query)
    conn.commit()
    conn.close()

    x = [ip , datetime.now().strftime('%Y%m%d%H%M%S')]
    print(x)

    return ",".join(x)

@app.route("/logout")
def logout():
    ip= request.remote_addr

    # junk
    global c

    table_setup_query = '''CREATE TABLE IF NOT EXISTS details (id integer primary key autoincrement, ip text, login timestamp, logout timestamp, duration number)'''
    c.execute(table_setup_query)

    q = [ val for ar in c.execute(f"select * from details where ip is '{ip}' order by login desc limit 1") for val in list(ar) ]

    duration_query = f"""update details set logout = datetime('now') , duration = strftime('%s', datetime('now') ) - strftime('%s', '{q[2]}' ) where id = {q[0]}"""

    c.execute( duration_query )
    conn.commit()
    conn.close()

    x = [ ip , datetime.now().strftime('%Y%m%d%H%M%S')]
    print(x)
    return ",".join(x)

if __name__ == "__main__":
    app.run()