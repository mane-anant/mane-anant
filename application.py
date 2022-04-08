from users import app
from users import config
from users import handlers
from flask import Flask, jsonify, request

app=app.app


@app.route('/hello', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "hello world"}
        return jsonify(data)