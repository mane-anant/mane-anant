from importlib.util import resolve_name
import json
from flask import request,jsonify
from users.app import app
from users.logic.response import response
from users.logic.data_songs import data_query




@app.route("/get/<audioFileType>/<audioFileId>",methods=['GET'])
@app.route("/get/<audioFileType>",methods=['GET'])
def getAudioFile(audioFileType,audioFileId=0):
    if (audioFileType=="song"):
        data=data_query.get_data(audioFileId)
        return data
            
    else:
        return response.bad_request()

#add data
@app.route("/add",methods=['POST'])
def addAudioFile():
    audioFileType=request.json["audioFileType"]
    audioFileMetaData=request.json["audioFileMetaData"]
    if audioFileType=='song':
        data_query.add_data(audioFileMetaData)
        return response.successful_request()

    else:
        return response.bad_request()


##DELETE DATA##############
@app.route("/delete/<audioFileType>/<audioFileId>",methods=['DELETE'])
def deleteAudioFile(audioFileType,audioFileId):
    if (audioFileType=='song'):
        data_query.delete_data(audioFileId)
        return response.successful_request()
    else:
        return response.bad_request()

#####UPDATE DATA#######
@app.route("/update/<audioFiletype>/<audioFileId>",methods=['PUT'])
def updateAudioFile(audioFiletype,audioFileId):
    audioFileMetaData=request.json["audioFileMetaData"]
    if (audioFiletype=='song'):
        data_query.update_data(audioFileId,audioFileMetaData)
        return response.successful_request()
    else:
        return response.bad_request()