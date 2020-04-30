from flask import Flask , request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    x = [request.remote_addr , datetime.now().strftime('%Y%m%d%H%M%S')]
    print(x)
    return ",".join( x )

app.run(threaded = True, port = 80)