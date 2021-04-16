"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User,Color,FavoriteColor
from api.utils import generate_sitemap, APIException
import requests

#* JWT libraries
from flask_jwt_extended import create_access_token
from flask_jwt_extended import current_user
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

# from .special_utilities.initialLoad import initial_loader
# from .special_utilities.payload_handlers import get_merged_lists,update_favorites_lists

from datetime import timedelta


api = Blueprint('api', __name__)


#* This method injects data to the database before receiving any foreign requests
@api.before_app_first_request
def characters_load():
    pass
    # user=User()
    # user.username="example_user"
    # user.email="example_email"
    # user.password="example_password"
    # user.is_active=True
    # db.session.add(user)
    # db.session.commit()

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