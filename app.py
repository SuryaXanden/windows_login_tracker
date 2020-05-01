from datetime import datetime
from flask import Flask, jsonify, render_template, request
import json

db = []
data_model = {
    "id" : 0,
    "ip" : "",
    "login" : "",
    "logout" : "",
    "duration" : 0
}

app = Flask(__name__)

@app.route("/" , methods = ["GET" , "POST"])
def index():
    if request.method == "GET":
        global db
        print(json.dumps(db))
        return render_template("index.html")
    if request.method == "POST":
        global db
        print(json.dumps(db))
        return jsonify(db)

@app.route("/login")
def login():
    ip = request.remote_addr

    global db
    global data_model

    doc = dict(data_model)

    last_id = db[-1]['id'] if len(db) else 0

    doc['id'] =  last_id + 1 if isinstance(last_id, int) else 1
    doc['ip'] = ip
    doc['login'] = datetime.now().strftime('%Y%m%d%H%M%S')
    
    db.append( doc )
    
    print(json.dumps(db))

    x = [ip , datetime.now().strftime('%Y%m%d%H%M%S')]

    return ",".join(x)

@app.route("/logout")
def logout():
    ip= request.remote_addr

    global db
    global data_model

    for i in range( len(db) , 0 , -1 ) :
        
        real_index_of_element = len(db)-i-1

        doc = db[ real_index_of_element ]

        if doc['ip'] == ip and doc['logout'] == "" and doc['login'] :
            now = datetime.now()
            rec = dict(data_model)

            rec['id'] = doc['id']
            rec['ip'] = doc['ip']
            rec['login'] = doc['login']
            rec['logout'] = now.strftime('%Y%m%d%H%M%S')
            rec['duration'] = int( (now - datetime.strptime( doc['login'] , '%Y%m%d%H%M%S' )).total_seconds() )

            db[ real_index_of_element ] = rec

            break
    
    print(json.dumps(db))

    x = [ ip , datetime.now().strftime('%Y%m%d%H%M%S')]
    return ",".join(x)

if __name__ == "__main__":
    app.run()