from flask import Flask, request
from flask_jsonrpc import JSONRPC

from mongoengine import connect, disconnect
from mgnmodel import RpcData, Role, User

from flask_admin import Admin
from flask_admin.contrib.mongoengine import ModelView

from flask_security import Security, MongoEngineUserDatastore, current_user

from utils import MyView

servrpc = Flask(__name__)
jsonrpc = JSONRPC(servrpc, '/api')

servrpc.config['SECRET_KEY'] = '12345667'
servrpc.config['SECURITY_PASSWORD_HASH'] = 'plaintext'
servrpc.config['SECURITY_PASSWORD_SALT'] = 'salt'

con = connect(
    host="mongodb+srv://filip:R6$h6g#NPZjzT&M@cluster0-mkw2o.mongodb.net/" +
    "test?retryWrites=true&w=majority"
)

user_datastore = MongoEngineUserDatastore(con, User, Role)
security = Security(servrpc, user_datastore)

admin = Admin(servrpc, index_view=MyView())
admin.add_view(ModelView(RpcData))
admin.add_view(ModelView(User))


def create_data(request, res):
    req = RpcData(
        md_method=str(request.json['method']),
        md_params=str(request.json['params']),
        md_result=res
    )
    req.save()


@jsonrpc.method('Servrpc.hello')
def hello(name):
    res = f'Hi {name},welcome to Flask JSON-RPC'
    create_data(request, res)
    return res


@jsonrpc.method('Servrpc.add')
def add_check_digit(barcode):
    s = barcode
    n = (sum(int(x) for x in s[1::2])) * 3 + (sum(int(x) for x in s[::2]))
    m = str(int(str(n)[:-1]) + 1) + '0'
    res = s + str(int(m) - n)
    create_data(request, res)
    return res


# user_datastore.create_user(email='admin@admin.com', password='123123')
if __name__ == '__main__':
    servrpc.run(debug=True)
