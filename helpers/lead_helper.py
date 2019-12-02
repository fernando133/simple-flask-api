from connection.db_connection import DBConnection
from helpers.telegram_helper import TelegramHelper
import datetime

class LeadHelper:
	def __init__(self):
		self.db = DBConnection()
		self.connection = self.db.get_connection()

	def str_to_bool(self, string):
	    if string == 'True':
	         return True
	    elif string == 'False':
	         return False

	def add_lead(name, email, origin, alert):
		pass

	def insert_lead(self, name, email, necessity, enterprise, role, state, city, phone, celphone, origin, alert):
		cursor = self.connection.cursor()
		now = datetime.datetime.utcnow()
		sql    = "INSERT INTO lead (name, email, necessity, enterprise, role, state, city, phone, celphone, origin, date_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
		val    = (name, email, necessity, enterprise, role, state, city, phone, celphone, origin, now)
		cursor.execute(sql, val)
		self.connection.commit()
		print(cursor.rowcount, "lead inserted.")
		alert = self.str_to_bool(alert)
		if(alert):
			th = TelegramHelper()
			th.broadcast_alert("Novo+Lead: ")

		return "200"

	def compute_access(self, origin):
		cursor = self.connection.cursor()
		sql    = "SELECT access_amount FROM campaing WHERE origin = '%s'" % origin
		cursor.execute(sql)
		amount = cursor.fetchall()
		amount = amount[0][0]
		new_amount = int(amount) + 1
		self.update_acess(origin, new_amount)

		return str(new_amount)

	def update_acess(self, origin, amount):
		cursor = self.connection.cursor()
		sql = "UPDATE campaing SET access_amount = '%s' WHERE origin = '%s'" % (amount, origin)
		cursor.execute(sql)
		self.connection.commit()
