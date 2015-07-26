#!/usr/bin/env python

from flask import Flask, jsonify, abort
from flask.ext.cors import CORS, cross_origin
from generator import Generator

app = Flask(__name__)
cors = CORS(app)
gen = Generator()

@app.route('/v1/list', methods=['GET'])
def list():
    data = {'data': gen.generate(), 'error': None}
    return jsonify(data)

@app.route('/v1/last', methods=['GET'])
def last():
    data = {'data': gen.last(), 'error': None}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host= '127.0.0.1', port=5000, debug=True)