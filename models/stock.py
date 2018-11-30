from db import db
from datetime import datetime

class StockModel(db.Model):
    __tablename__="stock"
    id = db.Column(db.Integer, primary_key=True)
    name_product = db.column(db.String(80))
    cantidad = db.Column(db.Integer)
    unidad = db.Column(db.String(80))
    price_total = db.Column(db.Float(pressision=2))
    fecha_vencimiento=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    producto_id=db.Column(db.Integer)
    
    def __init__(self, cantidad, unidad, price_total, producto_id):
        self.cantidad = cantidad
        self.unidad = unidad
        self.price_total = price_total
        self.producto_id = producto_id
    
    def json(self):
        return {
            'id': self.id,
            'cantidad': self.cantidad,
            'unidad': self.unidad,
            'price_total': self.price_total,
            'fecha_vencimiento': str(self.fecha_vencimiento),
            'producto_id': self.producto_id
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()
    @classmethod
    def find_by(cls):
        pass
