from models.product import ProductModel
from flask_restful import Resource, reqparse
import datetime as dt 
from datetime import datetime

import time
from models.entradas import EntradasModel
from models.stock import StockModel
from flask_jwt_extended import (
    jwt_required,
    jwt_optional, 
    get_jwt_identity
    )
#from models.salida import SalidaModel

_product_parse = reqparse.RequestParser()
_product_parse.add_argument('nombre_producto',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('fecha_vencimiento',
    #type=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%S'),
    type=lambda x: dt.datetime.strptime(x, "%Y-%m-%d").date(),
    #type=str,
    required=False,
    help="cannot be blank"
)
_product_parse.add_argument('cantidad',
    type=int,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('detalle_cantidad',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('unidad',
    type=int,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('detalle_unidad',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('tipo_medicamento',
    type=str,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('price_entrada',
    type=float,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('price_salida',
    type=float,
    required=True,
    help="cannot be blank"
)
_product_parse.add_argument('entrada_id',
    type=int,
    required=True,
    help="cannot be blank"
)

class RegisterProduct(Resource):
    @jwt_required
    def post(self):
        request_data = _product_parse.parse_args()
        #print("sadad: {}".format(request_data))
        #if ProductModel.find_by_nameproduct(request_data['nombre_producto']):
        #    return {"message": "el producto '{}' ya existe".format(request_data['nombre_producto'])}, 400
        

        psearch_if = [g.json() for g in ProductModel.find_all()]
        product = ProductModel.find_by_nameproduct(request_data['nombre_producto'])
        if product:
            #req = ProductModel.fin_by_pricesalid(request_data['nombre_producto'], request_data['price_salida'])
            
            aaa = product.json()['cantidad']
            bbb = product.json()['unidad']
            iddddd = product.json()['id']
            print("resss: {}".format(iddddd))
            product.cantidad = request_data['cantidad'] + aaa
            product.unidad = request_data['unidad'] + bbb
            
            #tipo_medicamento = ["analgecicos", "antiacidos", "antiulcerosos", "antialergicos", "laxantes", "antiinecciosos", "antiinflamatorios", "Antipiréticos", "Antitusivos", "mucolíticos"]

            #------if request_data[tipo_medicamento] = tipo_medicamento["analgesico"]:
            #------    product.unidad = request_data['cantidad']*200

            #stock = StockModel(request_data["cantidad"], request_data["detalle_unidad"], request_data['price_salida'], product.json()['cantidad'])

        else:
            product = ProductModel(**request_data)
                
        


        
        #a = "entrada de productos a la botica, mas abajo se detallan el nombre del producto y la cantidad que esta ingresando"
        #print(request_data['entrada_id'])
        #entrada = EntradasModel(a)
        #intentos = 0
        #while itentos < 10:
        #    d = request_data['entrada_id']
        #    entrada.save_to_db()s
        
        try:
            #stock.save_to_db()
            product.save_to_db()
            #salida.save_to_db()
        except:
            return {'message':'ah ocurrido un error al insertar el producto'}, 500
        
        return product.json(), 201


class ProductListOne(Resource):
    @jwt_required
    def get(self, nombre_producto):
        producto = ProductModel.find_by_nameproduct(nombre_producto)
        if producto:
            return producto.json()
        else:
            return {'message':'no se pudo encontrar el producto'}, 404


class ProductoList(Resource):
    @jwt_optional
    def get(self):
        #producto = [x.json() for x in ProductModel.find_all()]
        #return {'productos':producto}
        user_id = get_jwt_identity()
        productos = [x.json() for x in ProductModel.find_all()]
        if user_id:
            return {"productos":productos},200
        return {'prouctos':[producto['nombre_producto'] for producto in productos], 'message':'mode data available if you login'}

class ProductPoracAbarce(Resource):
    @jwt_required
    def get(self):

        producto = [x.json() for x in ProductModel.find_all()]
        #if x['cantidad'] <= 20 and x['cantidad'] > 0
        

        zz = [produss['cantidad'] for produss in producto]

        poco = [x for x in zz if x<=20 and x>0]
        a = []
        for i in poco:
            #print("ttt: {}".format(i))
            #ss = [y.json() for y in ProductModel.fin_by_cantidad(i)]
            #tt = ProductModel.find_by_date(i)
            tt = ProductModel.fin_by_cantidad(i)
            a.append(tt.json())
                
        return {"productos":a}
        #print("ssss: {}".format(poco))

        #return {'producto vencidos': producto}


class ProductEnd(Resource):
    @jwt_required
    def get(self):
        times = time.strftime("%Y-%m-%d")
        producto = [x.json() for x in ProductModel.find_all()]
        #ss = producto[0]a
        #productoend = [prduct['fecha_vencimiento'] for prduct in producto]
        aa = [produs['fecha_vencimiento'] for produs in producto] #if str(produs)==str(times)]
        #print("ssssssssssssssssss: {} and {}---------- {}".format(times, ss, aa))
        #if times == productoend:
        varialbe = [x for x in aa if x<=times]
        #query = ProductModel.find_by_date(str(varialbe))
        #ss = [y.json() for y in ProductModel.find_by_date(times)]
        a = []
        for i in varialbe:
            #print("ttt: {}".format(i))
            #ss = [y.json() for y in ProductModel.find_by_date(i)]
            tt = ProductModel.find_by_date(i)
            a.append(tt.json())
        return {"productos":a}
    
class ProductPorVender(Resource):
    def get(self):

        formato_fecha = "%Y-%m-%d"
        times = time.strftime(formato_fecha)
        producto = [x.json() for x in ProductModel.find_all()]
        fechas = [x['fecha_vencimiento'] for x in producto]
        
        variable = [x for x in fechas]
        ss = datetime.strptime(variable[0], formato_fecha)
        sd = datetime.strptime(times, formato_fecha)
        aa = ss - sd
        print("ssss: {}".format(aa.days))
        listaaa = []
        for s in fechas:
            aa = datetime.strptime(s, formato_fecha) - datetime.strptime(times, formato_fecha)
            aaa = [t for t in s if aa.days < 20]
            hh = "".join(aaa)
            if hh:
                data = ProductModel.find_by_date(hh)
                #print("kenyyy: {}".format(data.json()))
                print("aaaa: {}".format(data))
                listaaa.append(data.json())
                #return {"Productos por vencer": data.json()}


            #for n in aaa:
            #    print("xdddd: {}".format(n))
            #print("fechasssss:  {}".format(aa.days))
            #if aa.days < 20:
            #    print("it is True")
            #    aaa = [s for s in fechas if aa.days < 20]
            #    print("asdasd: {}".format(aaa))
           # else:
            #    print("you are nob")
        return {'productos': listaaa}
        










        #if varialbe:
        #    return query.json()
        #return {'message': query.json()}
        #   return {'message':'sss'}
        #return {'message': 'todos estan al dia'}

        
        
    
