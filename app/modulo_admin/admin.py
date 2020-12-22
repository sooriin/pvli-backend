from flask import request
from flask import jsonify
from flask import Blueprint
from daos.daoLevels import Level
from daos.daoUsers import Usuarios
from mongoengine.errors import NotUniqueError
from mongoengine.errors import ValidationError
from pymongo.errors import ServerSelectionTimeoutError

admin = Blueprint("admin", __name__)

@admin.route('/getStatistics', methods=['GET'])
def getStatistics():
    print("/getStatistics RECIBE", request.get_json())
    return jsonify({"return_code": "200"}), 200

@admin.route('/getAdminData', methods=['GET'])
def getAdminData():
    print("/getAdminData RECIBE", request.get_json())
    return jsonify({"return_code": "200"}), 200

@admin.route('/blockLevel', methods=['PUT'])
def blockLevel():
    print("/blockLevel RECIBE", request.get_json())
    return jsonify({"return_code": "200"}), 200

@admin.route('/unblockLevel', methods=['PUT'])
def unblockLevel():
    print("/unblockLevel RECIBE", request.get_json())
    return jsonify({"return_code": "200"}), 200

@admin.route('/blockUser', methods=['PUT'])
def blockUser():

    data = request.get_json()
    response = jsonify({"return_code": 200, "message": "OK"}), 200

    if ("username" in data):
        try:
            user = Usuarios.objects(username=data["username"])
            user.update_one(push__blocked=False)
            user = user.get()
            user.reload()
            response = jsonify({"return_code": 200, "message": "The user is blocked"}), 200
        except :
            response = jsonify({"return_code": 200, "message": "The user can`t be blocked"}), 601

    else:

        response = jsonify({"return_code": 400, "message": "Wrong Solicitation"}), 400

    return response
    
@admin.route('/unblockUser', methods=['PUT'])
def unblockUser():

    data = request.get_json()
    response = jsonify({"return_code": 200, "message": "OK"}), 200

    if ("username" in data):
        try:
            user = Usuarios.objects(username=data["username"])
            user.update_one(push__blocked=False)
            user = user.get()
            user.reload()
            response = jsonify({"return_code": 200, "message": "The user is unblocked"}), 200
        except :
            response = jsonify({"return_code": 200, "message": "The user can`t be unblocked"}), 601

    else:

        response = jsonify({"return_code": 400, "message": "Wrong Solicitation"}), 400

    return response