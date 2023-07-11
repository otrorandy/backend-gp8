
# A very simple Flask Hello World app for you to get started with...
# Importar
#  flask
# flask_cors
# flask_sqlalchemy
# flask_marshmallow

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


# CREAR LA APP
app = Flask(__name__)


# PERMITIR EL ACCESO DEL FRONTEND A LA RUTAS DE LAS APP
CORS(app)

# CONFIGURACIÓN A LA BASE DE DATOS                    //USER:PASSWORD@LOCALHOST/NOMBRE DB
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://crud23010grupo8:ejemplo1234@crud23010grupo8.mysql.pythonanywhere-services.com/crud23010grupo8$crud23010grupo82'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

# PERMITE MANIPULAR LA BASE DE DATOS DE LA APP
db = SQLAlchemy(app)
ma = Marshmallow(app)

# DEFINIR LA CLASE PRODUCTO (ESTRUCTURA DE LA TABLA DE UNA BASE DE DATOS)
class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(100))
    nombre = db.Column(db.String(100))
    precio = db.Column(db.Integer)
    stock = db.Column(db.Integer)
    imagen = db.Column(db.String(400))

    def __init__(self, categoria, nombre, precio,stock, imagen):
        self.categoria = categoria
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.imagen = imagen



# CÓDIGO QUE CREARÁ TODAS LAS TABLAS
with app.app_context():
    db.create_all()


# CLASE QUE PERMITIRÁ ACCEDER A LOS MÉTODOS DE CONVERSIÓN DE DATOS -  7
class ProductoSchema(ma.Schema):
    class Meta:
        fields = ("id", "categoria", "nombre", "precio", "stock", "imagen")


# CREAR DOS OBJETOS
producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)


@app.route('/')
def Inicio():
    return 'Bienvenido a la app rentals!'




# RUTAS
# '/productos' ENDPOINT PARA RECIBIR DATOS: POST
# '/productos' ENDPOINT PARA MOSTRAR TODOS LOS PRODUCTOS DISPONIBLES EN LA BASE DE DATOS: GET
# '/productos/<id>' ENDPOINT PARA MOSTRAR UN PRODUCTO POR ID: GET
# '/productos/<id>' ENDPOINT PARA BORRAR UN PRODUCTO POR ID: DELETE
# '/productos/<id>' ENDPOINT PARA MODIFICAR UN PRODUCTO POR ID: PUT

# ENDPOINT/RUTA
@app.route("/productos", methods=['GET'])
def get_productos():
    # CONSULTAR TODA LA INFO EN LA TABLA PRODUCTO
    all_productos = Producto.query.all()

    return productos_schema.jsonify(all_productos)





# RUTA CREAR UN NUEVO REGISTRO EN LA TABLA
@app.route("/productos", methods=['POST'])
def create_producto():

    """
    EJEMPLO:
    ENTRADA DE DATOS
    {
        "categoria": "ELECTRODOMESTICOS",
        "nombre": "MICROONDAS",
        "precio": 50000,
        "stock": 10,
        "imagen": "https://picsum.photos/200/300?grayscale",
    }

    """
    # RECIBEN LOS DATOS
    categoria = request.json['categoria']
    nombre = request.json['nombre']
    precio =request.json['precio']
    stock =request.json['stock']
    imagen = request.json['imagen']

    # INSERTAR EN DB
    new_producto = Producto(categoria, nombre, precio, stock, imagen)
    db.session.add(new_producto)
    db.session.commit()

    return producto_schema.jsonify(new_producto)


# MOSTRAR PRODUCTO POR ID
@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    producto=Producto.query.get(id)

   # Retorna el JSON de un producto recibido como parámetro
   # Para ello, usar el objeto producto_schema para que convierta con                   # jsonify los datos recién ingresados que son objetos a JSON
    return producto_schema.jsonify(producto)


# BORRAR
@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    producto=Producto.query.get(id)

    # A partir de db y la sesión establecida con la base de datos borrar
    # el producto.
    # Se guardan lo cambios con commit
    db.session.delete(producto)
    db.session.commit()

# MODIFICAR
@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    # Consultar por id, a la clase Producto.
    #  Se hace una consulta (query) para obtener (get) un registro por id
    producto=Producto.query.get(id)

    #  Recibir los datos a modificar
    categoria=request.json['categoria']
    nombre=request.json['nombre']
    precio=request.json['precio']
    stock=request.json['stock']
    imagen=request.json['imagen']

    # Del objeto resultante de la consulta modificar los valores
    producto.categoria=categoria
    producto.nombre=nombre
    producto.precio=precio
    producto.stock=stock
    producto.imagen=imagen
    #  Guardar los cambios
    db.session.commit()
   # Para ello, usar el objeto producto_schema para que convierta con                     # jsonify el dato recién eliminado que son objetos a JSON
    return producto_schema.jsonify(producto)