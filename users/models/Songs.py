import json
from flask_sqlalchemy import SQLAlchemy
from users.app import app


db=SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI']="mysql://root:root@localhost/practicdb"



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
