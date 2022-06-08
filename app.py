from flask import Flask, jsonify, request

import datetime

date = datetime.datetime.now()
unix_time = datetime.datetime.timestamp(date) * 1000
print(unix_time)

app = Flask(__name__)

req_rx = []


@app.route('/', methods=['GET'])
def hello():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.route('/test', methods=['GET'])
def item():
    return jsonify({"data": "New Hello World", "request_id": unix_time}), 200


@app.get("/auth")
def read_item():
    api_key = request.args.get('api_key')

    if api_key == '1234':
        return {'status': 'OK'}, 200
    return {'status': api_key}, 210


@app.get("/sendsms")
def sendSMS():
    api_key = request.args.get('api_key')
    number = request.args.get('number')
    d = {'status': 12345, "number": number, "api_key": api_key, 'args': request.args}
    req_rx.append(d)
    # if api_key == '1234':
    #     return {'status': 'OK'}, 200
    return {'status': 12345, "number": number, "api_key": api_key, 'args': request.args}, 200


@app.get("/report")
def report():
    return {'status': "OK", 'args': req_rx}, 200


if __name__ == '__main__':
    app.run(debug=True)
