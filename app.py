# -*- coding: utf-8 -*-
from flask import Flask
from flask import request, jsonify
import urllib2
import json
from helpers.email_helper import EmailHelper

import os
from flask import Flask, flash, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route("/testeEmail", methods=['GET', 'POST'])
def teste_email():
    email = EmailHelper(app)
    dest = "fernando.gmp@gmail.com"
    dest1 = "desenvolvimento@inlinetech.com.br"
    recipients=[dest, dest1]
    email.send_email("Teste", recipients, "Corpo do e-mail.")
    return "200"

@app.route("/enviar", methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def enviar_email():
	email = EmailHelper(app)
	data = request.form
	data = json.dumps(data)
	data = json.loads(data)
	emails, assunto, mensagem = data['email'], data['assunto'], data['mensagem']

	end = []
	end.append(emails)
	email.send_email(assunto, end, mensagem)

	return data
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
