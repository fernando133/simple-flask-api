from flask import Flask
from flask import request, jsonify
import urllib2
import json
from helpers.lead_helper import LeadHelper

app = Flask(__name__)
base_url = 'https://api.telegram.org/'
TOKEN = '1234'

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

@app.route("/addlead", methods=['POST'])
def insert_lead():
	data = request.json
	json_str = json.dumps(data)
	resp = json.loads(json_str)
	name, email, necessity, enterprise = resp['name'], resp['email'], resp['necessity'], resp['enterprise']
	role, state, city, phone, celphone = resp['role'], resp['state'], resp['city'], resp['phone'], resp['celphone']
	origin, alert = resp['origin'], resp['alert']
	return lh.insert_lead(name, email, necessity, enterprise, role, state, city, phone, celphone, origin, alert)
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)
