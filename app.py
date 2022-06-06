from flask import request, Flask, jsonify
import os

app = Flask(__name__)

@app.route("/login", methods=["GET"])
def login():
    userName: str = request.form.get("userName")
    password: str = request.form.get("password")
    response: dict= {"token": "61"}
    return jsonify(response)

@app.route("/register", methods=["POST"])
def register():
    userName: str = request.form.get("userName")
    password: str = request.form.get("password")
    response: dict= {"processCode": "1"}
    return jsonify(response)

@app.route("/logout", methods=["POST"])
def logout():
    userName: str = request.form.get("userName")
    response: dict= {"processCode": "1"}
    return jsonify(response)

def readEnvDataAsDict(path: str) ->dict:
    envVars:dict = {}
    with open(path, 'r') as file:
        for line in file:
            if(line.startswith('#') or not line.strip()):
                continue
            key, value = line.strip().split('=',1)
            envVars[key] = value
    return envVars

if __name__ == '__main__':
    variables = readEnvDataAsDict('local.env')
    host = variables.get("BASE_URL")
    port = variables.get("PORT")
    app.run(host = host, port = port, debug= True)