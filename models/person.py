from db import db

class PersonModel(db.Model):
	__tablename__="person"
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String(80))
	apellido = db.Column(db.String(80))

	def __init__(self, nombre, apellido):
		self.nombre = nombre
		self.apellido = apellido
	pass