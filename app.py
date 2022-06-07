from flask import Flask, jsonify, request

import datetime

date = datetime.datetime.now()
unix_time = datetime.datetime.timestamp(date)*1000
print(unix_time)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.get("/auth")
def read_item():
    api_key = request.args.get('api_key')

    if api_key == '1234':
        return {'status': 'OK'}, 200
    return {'status': api_key}, 210


if __name__ == '__main__':
    app.run(debug=True)
