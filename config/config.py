# -*- coding: utf-8 -*-
import os
import json

class Config:
	def __init__(self):
		file = open(os.path.abspath('config/script_conf.json'), 'r')
		self.conf = json.loads(file.read())
		self._conf_key = 'script-conf'

	def get_telegram_env(self,key):
		temp = self.conf[self._conf_key]
		temp = temp['telegram'][key]
		return str(temp)
		