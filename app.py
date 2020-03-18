# -*- coding: utf-8 -*-
from flask import Flask
from flask import request
import json
from helpers.email_helper import EmailHelper
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

@app.route("/enviar", methods=['POST'])
@cross_origin(origin='localhost',headers=['Content-Type'])
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
    app.run(host='0.0.0.0', port=5000)
