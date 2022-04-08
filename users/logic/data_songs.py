from users.models.Songs import Song,Process
from users.validations.schemas.SongSchema import songSchema,songsSchema
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy


class data_query():
    def get_data(audioFileId):
        if (audioFileId == 0):
            songs=Song.query.all()
            allsong=songsSchema.dump(songs)
            return jsonify(allsong)
        else:
            song=Song.query.get(audioFileId)
            songa=songSchema.dump(song)
            return jsonify(songa)

    def add_data(audioFileMetaData):
        newSong=Song(audioFileMetaData["id"],audioFileMetaData["name"],audioFileMetaData["Duration"],audioFileMetaData["Uploaded_time"])
        Process.add(newSong)
        Process.save()

    def delete_data(audioFileId):
        song=Song.query.get(audioFileId)
        Process.delete(song)
        Process.save()
    
    def update_data(audioFileId,audioFileMetaData):
        song=Song.query.get(audioFileId)
        song.id=audioFileMetaData["id"]
        song.name=audioFileMetaData["name"]
        song.Duration=audioFileMetaData["Duration"]
        song.Uploaded_time=audioFileMetaData["Uploaded_time"]
        Process.save()
