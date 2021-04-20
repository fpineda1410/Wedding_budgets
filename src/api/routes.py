"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Service1, Service2, Service3,BudgetItems
from api.utils import generate_sitemap, APIException
import requests

#* JWT libraries
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# from special_utilities.initialLoad import initial_loader
from .special_utilities.payload_handlers import get_merged_lists,update_favorites_lists

from datetime import timedelta


api = Blueprint('api', __name__)

#AQUI LUIS TIENE QUE VER LO SIGUIENTE
#VER QUE INFORMACION VA A SUBIR
#


#* This method injects data to the database before receiving any foreign requests
@api.before_app_first_request
# def characters_load():
#     user=User()
#     user.username="example_user"
#     user.email="example_email"
#     user.password="example_password"
#     user.is_active=True
#     db.session.add(user)
#     db.session.commit()

@api.route('/create-account', methods=['POST'])
def create_account():
    body=request.get_json()

    if body is None:
        return "The request body is null", 400
    if 'username' not in body:
        return "Empty username", 400
    if 'email' not in body:
        return "Empty email", 400
    if 'password' not in body:
        return "Empty password", 400
#todo modificar como se registra el usuario
    user=User()
    user.username=body['username']
    user.email=body['email']
    user.password=body['password']
    user.is_active=True
    db.session.add(user)
    db.session.commit()

    response_body = {
        "msg": "Added user"
    }
    return jsonify(response_body), 200
#todo modificar como se registra el usuario

#todo modificar como se loggea el usuario
@api.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).one_or_none()
    
    if not user or not user.check_password(password):
        return jsonify("Wrong username or password"), 401
    
    expiration=timedelta(hours=80)
    access_token = create_access_token(identity=user, expires_delta=expiration)

    return jsonify(access_token=access_token)
#todo modificar como se loggea el usuario

@api.route("/get-user-data" , methods=["GET"])
@jwt_required()
def get_favorites():
    pass
    #*--Check special_utilities/payload_handlers
    # merged_lists=get_merged_lists(current_user.id)
    # return jsonify(merged_lists), 200


@api.route("/update-user-data" , methods=["POST"])
@jwt_required()
def update_data_user():
    #*--Check special_utilities/payload_handlers
    user_payload=request.get_json()
    # updated_information=update_favorites_lists(user_payload,current_user.id)
    # return jsonify("Succesfully updated databases", updated_information), 200

@api.route("/get-budget" , methods=["GET"])
@jwt_required()
def get_budget():
    merged_lists=get_merged_lists(current_user.id)
    return jsonify(merged_lists), 200

@api.route("/update-budget" , methods=["POST"])
@jwt_required()
def update_budget_sm():
    user_payload=request.get_json()
    updated_lists=update_favorites_lists(user_payload,current_user.id)
    if updated_lists:
        currentBudget = BudgetItems.query.filter_by(user_id=current_user.id)
        currentBudgetList = list(map(lambda budget: budget.serialize(), currentBudget))
    return jsonify(currentBudgetList), 200
        # return jsonify("Succesfully updated databases"), 200


#!----Just use for debugging purposes
@api.route("/user_identity", methods=["GET"])
@jwt_required()
def protected():
    
    # We can now access our sqlalchemy User object via `current_user`.
    return jsonify(
        id=current_user.id,
        full_name=current_user.email,
        username=current_user.username,
    )

@api.route("/service1" , methods=['POST','GET'])
def get_serv1():    
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        
        service = Service1()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']

        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios

        return jsonify({"msg": "Well done. Your POSTED a service"}), 200

    elif request.method == 'GET':  
        return jsonify(Service1.getAllService()), 200

@api.route("/service2" , methods=['POST','GET'])
def get_serv2():   
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        
        service = Service2()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']

        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios

        return jsonify({"msg": "Well done. Your POSTED a service"}), 200

    elif request.method == 'GET':  
        return jsonify(Service2.getAllService()), 200

@api.route("/service3" , methods=['POST','GET'])
def get_serv3():    
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        
        service = Service3()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']

        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios

        return jsonify({"msg": "Well done. Your POSTED a service"}), 200

    elif request.method == 'GET':  
        return jsonify(Service3.getAllService()), 200

@api.route('/user', methods=['POST','GET'])
def handle_user():
    if request.method == 'POST':
        body = request.get_json()
        if body is None:
            return "The request body is null", 400
        if 'email' not in body:
            return "You need to specify the email", 400
        if 'username' not in body:
            return "You need to specify the username", 400
        if 'name' not in body:
            return "You need to specify the name", 400
        if 'last_name' not in body:
            return "You need to specify the last_name", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'password' not in body:
            return "You need to specify the password", 400
        
        user = User()
        user.email = body['email']
        user.username = body['username']
        user.name = body['name']
        user.last_name = body['last_name']
        user.phone = body['phone']
        user.password = body['password']
        user.is_active = True

        db.session.add(user) # agrega el usuario a la base de datos
        db.session.commit() # guarda los cambios

        response_body = {
            "msg": "Well done. Your POSTED an User"
        }

        return jsonify(response_body), 200
    
    elif request.method == 'GET':
        all_user = User.query.all()
        all_user = list(map(lambda x: x.serialize(), all_user))


        return jsonify(all_user), 200

@api.route("/allserv" , methods=["GET"])
def get_all():
    allService = {
        "flower": Service1.getAllService(),
        "location": Service2.getAllService(),
        "photo": Service3.getAllService(),
        # "music": Service4.getAllService()
    }
    return jsonify(allService), 200

@api.route('/listserv1', methods=['POST'])
def post_listserv1():
    listserv = request.get_json()
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service1()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios
    return jsonify({"msg": "Well done. Your POSTED a list of services 1"}), 200

@api.route('/listserv2', methods=['POST'])
def post_listserv2():
    listserv = request.get_json()
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service2()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios
    return jsonify({"msg": "Well done. Your POSTED a list of services 2"}), 200

@api.route('/listserv3', methods=['POST'])
def post_listserv3():
    listserv = request.get_json()
    for i in range(len(listserv)):
        body = listserv[i]
        if body is None:
            return "The request body is null", 400
        if 'category' not in body:
            return "You need to specify the category", 400
        if 'provider' not in body:
            return "You need to specify the provider", 400
        if 'description' not in body:
            return "You need to specify the description", 400
        if 'phone' not in body:
            return "You need to specify the phone", 400
        if 'price' not in body:
            return "You need to specify the price", 400
        service = Service3()
        service.category = body['category']
        service.description = body['description']
        service.provider = body['provider']
        service.phone = body['phone']
        service.price = body['price']
        db.session.add(service) # agrega un servicio a la base de datos
        db.session.commit() # guarda los cambios
    return jsonify({"msg": "Well done. Your POSTED a list of services 3"}), 200

@api.route("/allbudget" , methods=['GET'])
def get_allbudget():
    return jsonify(BudgetItems.getAllBudget()), 200



