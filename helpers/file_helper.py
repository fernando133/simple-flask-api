# -*- coding: utf-8 -*-

class FileHelper:
	def __init__(self):
		self.db = DBConnection()
		self.connection = self.db.get_connection()

	def allowed_file(filename):
    	return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
