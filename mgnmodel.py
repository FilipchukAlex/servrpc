from mongoengine import *

class RpcData(Document):
    md_method = StringField(max_length=20)
    md_params = StringField(max_length=150)
    md_result = StringField(max_length=150)
