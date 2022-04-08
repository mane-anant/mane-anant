from flask_marshmallow import Marshmallow
from ...app import app

ms=Marshmallow(app)


###schema for song
class SongSchema(ms.Schema):
    class Meta:
        fields=('id','name','Duration','Uploaded_time')

songSchema=SongSchema()
songsSchema=SongSchema(many=True)
