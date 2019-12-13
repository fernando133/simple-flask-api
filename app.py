# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify
import urllib2
import json
from helpers.lead_helper import LeadHelper
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_cors import CORS


UPLOAD_FOLDER = '/path/to/the/uploads'
base_url = 'https://api.telegram.org/'
TOKEN = '1234'


app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def authorize(_token):
	if _token == TOKEN:
		return True
	else:
		return False

@app.route("/lead/<name>/<email>/<necessity>/<enterprise>/<role>/<state>/<city>/<phone>/<celphone>/<origin>/<alert>", methods=['GET'])
def add_lead(name, email, necessity, enterprise, role, state, city, phone, celphone, origin, alert):
	lh = LeadHelper()
	return lh.insert_lead(name, email, necessity, enterprise, role, state, city, phone, celphone, origin, alert)

@app.route("/campaing/<origin>", methods=['GET'])
def compute_access(origin):
	lh = LeadHelper()
	return lh.compute_access(origin)

@app.route('/inscricao', methods=['POST'])
def nova_inscricao():
	data = request.form
	historico_escolar = None
	diploma = None
	try:
		if 'historico_escolar' in request.files:
			historico_escolar = request.files['historico_escolar']
			if historico_escolar.filename != '':
				historico_escolar.save(os.path.join('/home/inline/files', historico_escolar.filename))

		if 'diploma' in request.files:
			diploma = request.files['diploma']
			if diploma.filename != '':
				diploma.save(os.path.join('/home/inline/files', diploma.filename))
	except:
		return 500

	data = json.dumps(data)
	data = json.loads(data)
	lh = LeadHelper()
	return lh.nova_inscricao(data, historico_escolar.filename, diploma.filename)

@app.route("/broadcast", methods=['POST'])
def broadcast_post():
	data = request.json
	json_str = json.dumps(data)
	resp = json.loads(json_str)
	_token, bot, chat_id, msg = resp['token'], resp['bot'], resp['chat_id'], resp['msg']
	
	if authorize(_token):
		contents = urllib2.urlopen(base_url+bot+"/sendMessage?chat_id="+chat_id+"&text="+msg).read()
	else:
		return "invalid token"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
