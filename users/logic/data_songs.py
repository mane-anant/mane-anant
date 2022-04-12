from users.models.Songs import Song
from users.validations.schemas.SongSchema import songSchema,songsSchema
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy



def get_data(audioFileId):
    if (audioFileId == 0):
        songs=Song.allQuery()
        allsong=songsSchema.dump(songs)
        return jsonify(allsong)
    else:
        song=Song.singleQuery(audioFileId)
        songa=songSchema.dump(song)
        return jsonify(songa)

def add_data(audioFileMetaData):
    newSong=Song(audioFileMetaData["id"],audioFileMetaData["name"],audioFileMetaData["Duration"],audioFileMetaData["Uploaded_time"])
    Song.add(newSong)
    Song.save()

def delete_data(audioFileId):
    song=Song.singleQuery(audioFileId)
    Song.delete(song)
    Song.save()

def update_data(audioFileId,audioFileMetaData):
    song=Song.singleQuery(audioFileId)
    song.id=audioFileMetaData["id"]
    song.name=audioFileMetaData["name"]
    song.Duration=audioFileMetaData["Duration"]
    song.Uploaded_time=audioFileMetaData["Uploaded_time"]
    Song.save()
