from flask import Flask, jsonify, request
import typing
import time
import datetime

date = datetime.datetime.now()
unix_time = datetime.datetime.timestamp(date)*1000
print(unix_time)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def helloworld():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.route('/new', methods=['GET'])
def helloworld():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.route('/test', methods=['GET'])
def helloworld():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.route('/', methods=['GET'])
def helloworld():
    return jsonify({"data": "Hello Jyotsna ", "request_id": unix_time}), 200


@app.get("/auth")
def read_item(api_key: typing.Union[str, None] = None):
    if api_key == '1234':
        return {'status': 'OK'}, 200
    return {'status':''}, 210


if __name__ == '__main__':
    app.run(debug=True)
