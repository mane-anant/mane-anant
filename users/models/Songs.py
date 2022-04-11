import json
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from ..app import app


db = SQLAlchemy(app)

class Song(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(30),nullable=False)
    Duration=db.Column(db.Integer,nullable=False)
    Uploaded_time=db.Column(db.DateTime,nullable=False)

    def __init__(self,id,name,Duration,Uploaded_time):
        self.id=id
        self.name=name
        self.Duration=Duration
        self.Uploaded_time=Uploaded_time
        

    def add(data):
        return db.session.add(data)
    def save():
        return db.session.commit()
    def delete(data1):
        return db.session.delete(data1)
    def allQuery():
        return Song.query.all()
    def singleQuery(audioFileId):
        return Song.query.get(audioFileId)


        # add=db.session.add()
        # save=db.session.commit()
        # elete=db.session.delete()