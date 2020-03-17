# -*- coding: utf-8 -*-
from flask_mail import Mail, Message
import os
from flask import render_template


class EmailHelper:

    def __init__(self, app):
        self.mail_settings = {
            "MAIL_SERVER": os.environ['MAIL_SERVER'],
            "MAIL_PORT": os.environ['MAIL_PORT'],
            #"MAIL_USE_TLS": True,
            "MAIL_USE_SSL": True,
            "MAIL_USERNAME": os.environ['EMAIL_USER'],
            "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
        }
        self.app = app
        self.app.config.update(self.mail_settings)
        self.e_mail = Mail(self.app)


    def send_email(self, subject, recipients, body):
        msg = Message(subject=subject,
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=recipients)
        msg.html=render_template('basic-email.html', email_body = body)

        self.e_mail.send(msg)
