from flask import request, Flask

app = Flask(__name__)

@app.route("/login", methods=["GET"])
def login():
    userName: str = request.form.get("userName")
    password: str = request.form.get("password")
    response: dict= {"token": "61"}
    return response

@app.route("/register", methods=["POST"])
def login():
    userName: str = request.form.get("userName")
    password: str = request.form.get("password")
    response: dict= {"processCode": "1"}
    return response

@app.route("/logout", methods=["POST"])
def login():
    userName: str = request.form.get("userName")
    response: dict= {"processCode": "1"}
    return response

if __name__ == '__main__':
    host = "127.0.0.1"
    port = "6061"
    app.run(host = host, port = port, debug= True)