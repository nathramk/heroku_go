from db import db
from datetime import datetime

class SalidaModel(db.Model):
    __tablename__="salidas"
    id = db.Column(db.Integer, primary_key=True)
    detalle = db.Column(db.String(80))
    fecha_salida = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    def __init__(self, detalle):
        self.detalle = detalle
    def json(self):
        return {
            "id":self.id,
            "detalle":self.detalle,
            "fecha_salida":self.fecha_salida
        }

    @classmethod
    def find_all_salidas(cls):
        return cls.query.all()
    @classmethod
    def find_by_id(cls, salida_id):
        return cls.query.filter_by(id=salida_id).first()

    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    