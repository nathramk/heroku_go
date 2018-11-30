from flask_restful import Resource, reqparse
from models.stock import StockModel


_data_parser = reqparse.RequestParser()

_data_parser.add_argument('cantidad',
    type=int,
    required=True,
    help="O bien estas mandando el campo vacio, o es el tipo de dato incorrecto que estas ingresando"

)
_data_parser.add_argument('unidad',
    type=str,
    required=True,
    help="O bien estas mandando el campo vacio, o es el tipo de dato incorrecto que estas ingresando"
)
_data_parser.add_argument('price_total',
    type=int,
    required=True,
    help="O bien estas mandando el campo vacio, o es el tipo de dato incorrecto que estas ingresando"
)
_data_parser.add_argument('producto_id',
    type=int,
    required=True,
    help="O bien estas mandando el campo vacio, o es el tipo de dato incorrecto que estas ingresando"
)

class RegistarStock(Resource):
    def post(self):
        data = _data_parser.parse_args()
        stock = StockModel(**data)
        try:
            stock.save_to_db()
        except:
            return {"message":"Ocurrio un error al ingresar un dato a la base de datos."}, 500
        
        return stock.json()

class ListEstock(Resource):
    def get(self):
        stock = [x.json() for x in StockModel.find_all()]
        return {'stock':stock}