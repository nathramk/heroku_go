from db import db
from datetime import datetime
import time

class ProductModel(db.Model):
	__tablename__ = 'products'
	id = db.Column(db.Integer, primary_key=True)
	nombre_producto = db.Column(db.String(80))
	fecha_vencimiento = db.Column(db.Date, nullable=False)#, default=datetime.utcnow)#, default=datetime.utcnow)
	cantidad = db.Column(db.Integer)
	detalle_cantidad = db.Column(db.String(80))
	unidad = db.Column(db.Integer)
	detalle_unidad = db.Column(db.String(80))
	tipo_medicamento = db.Column(db.String(80))
	price_entrada = db.Column(db.Float(precision=2))
	price_salida = db.Column(db.Float(precision=2))
	entrada_id = db.Column(db.Integer, db.ForeignKey('entradas.id'))

	entrada = db.relationship('EntradasModel')

	def __init__(self, nombre_producto,fecha_vencimiento,cantidad,detalle_cantidad,unidad,detalle_unidad,tipo_medicamento,price_entrada, price_salida,entrada_id):
		self.nombre_producto = nombre_producto
		self.fecha_vencimiento = fecha_vencimiento
		self.cantidad = cantidad
		self.detalle_cantidad = detalle_cantidad
		self.unidad = unidad
		self.detalle_unidad = detalle_unidad
		self.tipo_medicamento = tipo_medicamento
		self.price_entrada = price_entrada
		self.price_salida = price_salida
		self.entrada_id = entrada_id
	
	def json(self):
		return {
			'id': self.id,
			'nombre_producto': self.nombre_producto,
			'fecha_vencimiento': str(self.fecha_vencimiento),
			'cantidad': self.cantidad,
			'detalle_cantidad':self.detalle_cantidad,
			'unidad': self.unidad,
			'detalle_unidad':self.detalle_unidad,
			'tipo_medicamento':self.tipo_medicamento,
			'price_entrada': self.price_entrada,
			'price_salida': self.price_salida,
			'entrada_id': self.entrada_id
		}

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()
	
	
	@classmethod
	def find_by_nameproduct(cls, nombre_producto):
		producto = cls.query.filter_by(nombre_producto=nombre_producto).first()
		return producto
	
	@classmethod
	def find_by_productId(cls, _id):
		producto = cls.query.filter_by(id=_id).first()
		return producto
	
	@classmethod
	def find_all(cls):
		producto = cls.query.all()
		return producto

	@classmethod	
	def find_by_date(cls, fecha_vencimiento):
		
		product = cls.query.filter_by(fecha_vencimiento=fecha_vencimiento).first()
		
		return product
	@classmethod
	def fin_by_cantidad(cls, cantidad):
		#produ = cls.query.filter_by(nombre_producto=nombre_producto).filter_by(price_salida=price_salida).first()
		produ = cls.query.filter_by(cantidad=cantidad).first()
		return produ