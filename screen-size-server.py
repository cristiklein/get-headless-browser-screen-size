#!/usr/bin/env python
from flask import Flask, request
import logging

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/report-size')
def reportSize():
	documentHeight = request.args.get('document_height')
	documentWidth  = request.args.get('document_width')
	windowHeight = request.args.get('window_height')
	windowWidth  = request.args.get('window_width')

	logging.warn("document=(%s,%s), window=(%s,%s)", documentWidth, documentHeight, windowWidth, windowHeight)

	return 'Okey'

if __name__ == '__main__':
	app.run(debug=True,port=7777)
