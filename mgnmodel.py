from mongoengine import *
from flask_security import UserMixin, RoleMixin

class RpcData(Document):
    md_method = StringField(max_length=20)
    md_params = StringField(max_length=150)
    md_result = StringField(max_length=150)

class Role(Document, RoleMixin):
    name = StringField(max_length=50, unique=True)

    def __unicode__(self):
        return self.name

class User(Document, UserMixin):
    email = StringField(max_length=50, unique=True)
    password = StringField(max_length=50)
    active = BooleanField(default=True)
    roles = ListField(ReferenceField(Role), default=[])

    def __unicode__(self):
        return self.name
