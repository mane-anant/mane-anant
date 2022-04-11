from flask import Flask
from users.config import practicdb



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=practicdb