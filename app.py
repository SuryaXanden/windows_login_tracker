from flask import Flask , request
# from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
# CORS(app)

@app.route("/")
def index():
    x = [request.remote_addr , datetime.now().strftime('%Y%m%d%H%M%S')]
    print(x)
    return ",".join( x )

# app.run(threaded = True, host='0.0.0.0')
# app.run(host='0.0.0.0')
if __name__ == "__main__":
    app.run()