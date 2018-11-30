from db import db

class UserModel(db.Model):
	__tablename__='users'
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(80))
	password = db.Column(db.String(80))

	def __init__(self, email, password):
		self.email=email
		self.password=password
	
	def json(self):
		return {
			'id': self.id,
			'email': self.email
		}
	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	@classmethod
	def fin_by_email(cls, email):
		return cls.query.filter_by(email=email).first()
	
	@classmethod
	def fin_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()
