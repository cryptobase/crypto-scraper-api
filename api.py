#!/usr/bin/env python

from flask import Flask, jsonify, abort, render_template
from flask.ext.cors import CORS, cross_origin
from generator import Generator
import argparse

app = Flask(__name__)
cors = CORS(app)
gen = None  #Generator()


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='API Documentation')


@app.route('/v1/list', methods=['GET'])
def list():
    data = {'data': gen.generate(), 'error': None}
    return jsonify(data)


@app.route('/v1/last', methods=['GET'])
def last():
    data = {'data': gen.last(), 'error': None}
    return jsonify(data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scraper data REST api.')
    parser.add_argument('-p', '--path', help="Path to data files")

    args = parser.parse_args()
    gen = Generator(args.path)

    app.run(host='0.0.0.0', port=5000, debug=True)
