# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify
import urllib2
import json
from helpers.lead_helper import LeadHelper
import os
from flask import Flask, flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS
import datetime
import calendar
import time

UPLOAD_FOLDER = '/home/inline/files'
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

def link_pagamento(foco_aulas):
    if foco_aulas == "Superior":
        return "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=170979160-35cea3f4-9493-4f79-8c10-28d2f49240c0"
    elif foco_aulas == "Medio Tecnico":
        return "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=170979160-8c3b3867-c461-4b87-8706-c50dad81f746"
    elif foco_aulas == "Fundamental":
        return "https://www.mercadopago.com.br/checkout/v1/redirect?pref_id=170979160-ab29a5f6-b118-45e2-b768-83dde14a1a70"

def get_file_name(filename):
    ts = calendar.timegm(time.gmtime())
    filename = str(ts)+filename
    return filename

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
    curriculo_name = None

    try:
        if 'historico_escolar' in request.files:
            historico_escolar = request.files['historico_escolar']
            if historico_escolar.filename != '':
                historico = get_file_name(historico_escolar.filename)
                historico_escolar.save(os.path.join(app.config['UPLOAD_FOLDER'], historico))

        if 'diploma' in request.files:
            diploma = request.files['diploma']
            if diploma.filename != '':
                diploma_name = get_file_name(diploma.filename)
                diploma.save(os.path.join(app.config['UPLOAD_FOLDER'], diploma_name))

        if 'curriculo' in request.files:
            curriculo = request.files['curriculo']
            if curriculo.filename != '':
                curriculo_name = get_file_name(curriculo.filename)
                curriculo.save(os.path.join(app.config['UPLOAD_FOLDER'], curriculo_name))

    except Exception as e:
        print e

    data = json.dumps(data)
    data = json.loads(data)
    lh = LeadHelper()
    nova_inscricao = lh.nova_inscricao(data, historico, diploma_name, curriculo_name)
    nova_inscricao = bool(nova_inscricao)
    if nova_inscricao:
        return render_template('inscricao-sucesso.html', link = link_pagamento(data['foco_aulas']))
    else:
        return render_template('inscricao-erro.html')

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
