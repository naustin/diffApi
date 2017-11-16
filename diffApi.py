from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/')
def healthcheck():
    return 'Hello!'

@app.route('/getdiff', methods=['POST'])
def getdiff():
    if not request.json:
        return "no json received"

    if request.json:
        mydata = request.json
        return mydata.get("doc1")

   
        
    