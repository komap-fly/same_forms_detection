from flask import Flask, request
from .utils import _gen_error, generate_response


class Server:

    def __init__(self, key: str):
        self.key = key
        app = Flask(__name__)
        self.app = app

    def handle_response(self):
        headers = request.headers
        if headers.get('content-type') != 'application/json':
            return _gen_error('wrong content-type')
        if headers.get('key') != self.key:
            return _gen_error('wrong key')
        try:
            sentence = request.json['sentence']
        except (KeyError, TypeError):
            return _gen_error('sentence key is not in JSON!')
        return generate_response(phrase=sentence)

    def start_server(self, port=5000, host='0.0.0.0'):
        self.app.route('/', methods=['POST'])(self.handle_response)
        self.app.run(host=host, port=port)
