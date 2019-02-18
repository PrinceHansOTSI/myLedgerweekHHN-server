from flask import Flask, request
server = Flask(__name__)

@server.route('/', methods = ['GET'])
def main():
    return "We're alive!"

@server.route('/api/accounts', methods = ['POST'])
def accounts():
    json = request.get_json()
    if json['devid']:
        print(json['devid'])
    return "we did it"