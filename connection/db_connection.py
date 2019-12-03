# -*- coding: utf-8 -*-
import mysql.connector

class DBConnection:

	def __init__(self):
		self.localhost = '127.0.0.1'
		self.username  = 'root'
		self.password  = 'root'
		self.database  = 'flask'

	def get_connection(self):
		mydb     = mysql.connector.connect(
  		host     = self.localhost,
  		user     = self.username,
  		passwd   = self.password,
  		database = self.database
		)
		return mydb
