"This is for the json response if any error occurs"

import json
from flask import jsonify

##for bad response

def bad_request():
    return jsonify({"Request is invalid":"400 bad request"}),400

def successful_request():
    return jsonify({"Action is successful": "200 OK"}),200