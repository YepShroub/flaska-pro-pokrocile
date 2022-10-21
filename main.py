import datetime

import flask
from flask import Flask
from flask import request

app = Flask(__name__)

messages = ["cau", "zdar", "gugu gaga"]


@app.route('/')
def index():
    return 'Vitejte na serveru SPSE Jecna'


@app.route('/zkouska')
def moje_zkouska():
    return 'Možná budou funovat i háčky a čárky.'


@app.route('/restapi/v1/user/<username>', methods=['GET'])
def user_show(username):
    return "Ahoj "+username


@app.route('/restapi/v1/user/<username>', methods=['DELETE'])
def user_delete(username):
    return "Uzivatel "+username+" byl smazan"


@app.route('/restapi/v1/datetime', methods=['GET'])
def datetime_show():
    return {"links": [
            {
                "href": "/datetime/date",
                "rel": "get current date",
                "type": "GET"
            },
            {
                "href": "/datetime/time",
                "rel": "get current time",
                "type": "GET"
            },
            {
                "href": "/datetime/cz",
                "rel": "get current date and time in cz format",
                "type": "GET"
            },
            {
                "href": "/datetime/iso",
                "rel": "get current date and time in iso format",
                "type": "GET"
            }
            ]
            }


@app.route('/restapi/v1/datetime/date', methods=['GET'])
def date_show():
    return {"date": str(datetime.datetime.now().date())}


@app.route('/restapi/v1/datetime/time', methods=['GET'])
def time_show():
    return {"time": str(datetime.datetime.now().time())}


@app.route('/restapi/v1/datetime/cz', methods=['GET'])
def cz_time_show():
    return {"cz_time": str(datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S"))}


@app.route('/restapi/v1/datetime/iso', methods=['GET'])
def iso_time_show():
    return {"iso_time": str(datetime.datetime.now().isoformat())}


@app.route('/restapi/v1/messages', methods=['GET'])
def messages_show():
    return {"messages": {i: m for i, m in enumerate(messages)},
            "links": [
                {
                    "href": "/messages/<id>",
                    "rel": "get a message by id",
                    "type": "GET"
                },
                {
                    "href": "/messages/send",
                    "rel": "send a new message",
                    "type": "POST"
                },
                {
                    "href": "/messages/delete",
                    "rel": "delete a message by id",
                    "type": "DELETE"
                },
                {
                    "href": "/messages/edit/<id>",
                    "rel": "edit a message by id",
                    "type": "POST"
                }
            ]}


@app.route('/restapi/v1/messages/<mid>', methods=['GET'])
def message_show_by_id(mid):
    try:
        return messages[int(mid)]
    except IndexError:
        flask.abort(404)


@app.route('/restapi/v1/messages/send', methods=['POST'])
def message_send():
    messages.append(request.json["message"])
    return flask.jsonify(success=True)


@app.route('/restapi/v1/messages/<mid>', methods=['DELETE'])
def message_delete(mid):
    try:
        messages.pop(int(mid))
    except IndexError or ValueError:
        flask.abort(404)
    return flask.jsonify(success=True)


@app.route('/restapi/v1/messages/<mid>', methods=['PUT'])
def message_edit(mid):
    try:
        messages[int(mid)] = request.json["message"]
    except IndexError or ValueError:
        flask.abort(404)
    return flask.jsonify(success=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
