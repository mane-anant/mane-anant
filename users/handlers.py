import json
from flask import request,jsonify
from users.app import app
from users.models.Songs import Song,db
from users.validations.schemas.SongSchema import songSchema,songsSchema


db=db
@app.route("/get/<audioFileType>/<audioFileId>",methods=['GET'])
@app.route("/get/<audioFileType>",methods=['GET'])
def getAudioFile(audioFileType,audioFileId=0):
    if (audioFileType=="song"):
        if (audioFileId == 0):
            songs=Song.query.all()
            allsong=songsSchema.dump(songs)
            return jsonify(allsong)
        else:
            song=Song.query.get(audioFileId)
            songa=songSchema.dump(song)
            return jsonify(songa)

    else:
        return jsonify({"Request is invalid":"400 bad request"}),400

#add data
@app.route("/add",methods=['POST'])
def addAudioFile():
    audioFileType=request.json["audioFileType"]
    audioFileMetaData=request.json["audioFileMetaData"]
    if audioFileType=='song':
        newSong=Song(audioFileMetaData["id"],audioFileMetaData["name"],audioFileMetaData["Duration"],audioFileMetaData["Uploaded_time"])
        db.session.add(newSong)
        db.session.commit()
        return jsonify({"Action is successful": "200 OK"}),200

    else:
        return jsonify({"Request is invalid":"400 bad request"}),400


##DELETE DATA##############
@app.route("/delete/<audioFileType>/<audioFileId>",methods=['DELETE'])
def deleteAudioFile(audioFileType,audioFileId):
    if (audioFileType=='song'):
        song=Song.query.get(audioFileId)
        db.session.delete(song)
        db.session.commit()
        return jsonify({"Action is successful": "200 OK"}),200
    else:
        return jsonify({"Invalid request":"404 error"}),400

#####UPDATE DATA#######
@app.route("/update/<audioFiletype>/<audioFileId>",methods=['PUT'])
def updateAudioFile(audioFiletype,audioFileId):
    audioFileMetaData=request.json["audioFileMetaData"]
    if (audioFiletype=='song'):
        song=Song.query.get(audioFileId)
        song.id=audioFileMetaData["id"]
        song.name=audioFileMetaData["name"]
        song.Duration=audioFileMetaData["Duration"]
        song.Uploaded_time=audioFileMetaData["Uploaded_time"]
        db.session.commit()
        return jsonify({"Action is successful": "200 OK"}),200
    else:
        return jsonify({"Invalid request":"404 error"}),400