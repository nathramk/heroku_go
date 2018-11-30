from models.salida import SalidaModel
from flask_restful import Resource, reqparse

_product_parse = reqparse.RequestParser()
_product_parse.add_argument('detalle',
    type=str,
    required=True,
    help="cannot be blank"
)

class RegisterSalida(Resource):
    def post(self):
        data = _product_parse.parse_args()
        salida = SalidaModel(data)

        try:
            salida.save_to_db()
        except:
            return {"message": "ocurrio un problea insertando a la base de datos"}, 500
        return salida.json(), 201

class ListSalida(Resource):
    def get(self):
        pass