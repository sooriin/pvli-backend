from flask import request
from flask import jsonify
from flask import Blueprint
from daos.daoUsers import Usuarios
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError
from pymongo.errors import ServerSelectionTimeoutError

users = Blueprint("users", __name__)

@users.route('/newUser', methods=['POST'])
def newUser():

    data = request.get_json()
    response = jsonify({"return_code": 200, "message": "OK"}), 200

    if ("username" in data) and ("password" in data):

        try:
            Usuarios(username=data["username"], password=data["password"], blocked=data["blocked"]).save(force_insert=True)
        except NotUniqueError:
            response = jsonify({"return_code": 601, "message": 'El usuario ya existe'}), 601
        except ValidationError:
            response = jsonify({"return_code": 400, "message": "Solicitud incorrecta"}), 400
        except ServerSelectionTimeoutError:
            response = jsonify({"return_code": 500, "message": "No se puede conectar con la base de datos"}), 500

    else:

        response = jsonify({"return_code": 400, "message": "Solicitud incorrecta"}), 400

    return response

     -
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
# OJO QUE LO MISMO HAY QUE HACER LA POLLA DE GOGLE
@users.route('/login', methods=['POST'])
def login():
    print("/login RECIBE", request.get_json())
    return jsonify({"return_code": "200"}), 200
