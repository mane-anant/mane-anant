from importlib.util import resolve_name
import json
from flask import request,jsonify
from users.app import app
from users.logic.response import bad_request,successful_request
from users.logic.data_songs import get_data,add_data,delete_data,update_data




@app.route("/get/<audioFileType>/<audioFileId>",methods=['GET'])
@app.route("/get/<audioFileType>",methods=['GET'])
def getAudioFile(audioFileType,audioFileId=0):
    if (audioFileType=="song"):
        data=get_data(audioFileId)
        return data
            
    else:
        return bad_request()

#add data
@app.route("/add",methods=['POST'])
def addAudioFile():
    import pdb; pdb.set_trace()
    audioFileType=request.json["audioFileType"]
    audioFileMetaData=request.json["audioFileMetaData"]
    if audioFileType=='song':
        add_data(audioFileMetaData)
        return successful_request()

    else:
        return bad_request()


##DELETE DATA##############
@app.route("/delete/<audioFileType>/<audioFileId>",methods=['DELETE'])
def deleteAudioFile(audioFileType,audioFileId):
    if (audioFileType=='song'):
        delete_data(audioFileId)
        return successful_request()
    else:
        return bad_request()

#####UPDATE DATA#######
@app.route("/update/<audioFiletype>/<audioFileId>",methods=['PUT'])
def updateAudioFile(audioFiletype,audioFileId):
    audioFileMetaData=request.json["audioFileMetaData"]
    if (audioFiletype=='song'):
        update_data(audioFileId,audioFileMetaData)
        return successful_request()
    else:
        return bad_request()