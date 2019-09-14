from flask import Flask
from flask_jsonrpc import JSONRPC

servrpc = Flask(__name__)
jsonrpc = JSONRPC(servrpc, '/api')


@jsonrpc.method('Servrpc.hello')
def hello(name):
    return f'Hi {name},welcome to Flask JSON-RPC'


@jsonrpc.method('Servrpc.add')
def add_check_digit(barcode):
    s = barcode
    n = (sum(int(x) for x in s[1::2])) * 3 + (sum(int(x) for x in s[::2]))
    m = str(int(str(n)[:-1]) + 1) + '0'
    return s + str(int(m) - n)


if __name__ == '__main__':
    servrpc.run(debug=True)
