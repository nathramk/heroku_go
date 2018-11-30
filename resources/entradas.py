from models.entradas import EntradasModel
from flask_restful import Resource, reqparse
_entrada_parser = reqparse.RequestParser()
from flask_jwt_extended import (
    jwt_required,
    jwt_optional, 
    get_jwt_identity
)

_entrada_parser.add_argument('detalle',
    type=str,
    required=True,
    help="No dberia de estar en blanco"
)
_entrada_parser.add_argument('nombre_proveedor',
    type= str,
    required=True,
    help="cannot be blank"
)

class RegistrarEntradas(Resource):
    @jwt_required
    def post(self):
        data = _entrada_parser.parse_args()
        #if EntradasModel.find_by_id.
        #entrada = EntradasModel.find_by_id()
        entrada = EntradasModel(**data)
        try:
            entrada.save_to_db()
        except:
            return {"message":"ocurrio un error al isertar una nueva entrada"}, 500

        return entrada.json(),201

class EntradaGet(Resource):
    @jwt_required
    @classmethod
    def get(cls, entrada_id):
        entrada = EntradasModel.find_by_id(entrada_id)
        if not entrada:
            return {'message':'no se pudo encontrar la entrada'}
        return entrada.json()
        


class EntradasList(Resource):
    @jwt_required
    def get(self):
        entrada = [x.json() for x in EntradasModel.find_all()]
        return {'entradas': entrada}
