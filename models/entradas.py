from db import db
from datetime import datetime

class EntradasModel(db.Model):
    __tablename__ = 'entradas'
    id = db.Column(db.Integer, primary_key=True)
    detalle = db.Column(db.String(80))
    fecha_ingreso = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    nombre_proveedor = db.Column(db.String(80))
    producto = db.relationship('ProductModel', lazy='dynamic')
    def __init__(self, detalle, nombre_proveedor):
        self.detalle = detalle
        self.nombre_proveedor = nombre_proveedor
    
    def json(self):
        return {
            'id':self.id,
            'detalle':self.detalle,
            'fecha_ingreso':str(self.fecha_ingreso),
            'nombre_proveedor': self.nombre_proveedor,
            'producto': [producto.json() for producto in self.producto.all()]
        }
    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        