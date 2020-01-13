# -*- coding: utf-8 -*-
from config.config import Config
import urllib2
import telepot

class TelegramHelper:

    def __init__(self):
        cfg = Config()
        self.base_url = 'https://api.telegram.org/'
        self.bot_id   = cfg.get_telegram_env('bot_id')
        self.chat_id  = cfg.get_telegram_env('chat_id')

    def get_error_msg(self, error):
        error = error.split(" ")
        error_prc = 'err:+'
        for item in error:
            error_prc =  error_prc + item + '+'
        return error_prc

    def broadcast_alert(self, msg):
        urllib2.urlopen(self.base_url+self.bot_id+"/sendMessage?chat_id="+self.chat_id+"&text="+msg).read()

    def broadcast(self, msg):
        try:
            bot=telepot.Bot(self.bot_id)
            bot.sendMessage(self.chat_id, msg)
        except Exception as e:
            return str(e)
