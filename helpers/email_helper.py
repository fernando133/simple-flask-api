from flask_mail import Mail, Message
import os

class EmailHelper:
    
    def __init__(self, app):
        self.mail_settings = {
            "MAIL_SERVER": 'smtp.gmail.com',
            "MAIL_PORT": 465,
            "MAIL_USE_TLS": False,
            "MAIL_USE_SSL": True,
            "MAIL_USERNAME": os.environ['EMAIL_USER'],
            "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
        }
        self.app = app
        self.app.config.update(self.mail_settings)
        self.e_mail = Mail(self.app)


    def send_email(self, subject, recipients, body):
        print subject, recipients, body, self
        msg = Message(subject=subject,
                      sender=self.app.config.get("MAIL_USERNAME"),
                      recipients=recipients, # replace with your email for testing
                      body=body)
        
        self.e_mail.send(msg)
