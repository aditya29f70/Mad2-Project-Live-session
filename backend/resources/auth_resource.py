"/login"
"/register"

from flask import Blueprint, request, jsonify
from flask_security.utils import verify_password

from model import User

auth_bp= Blueprint("auth",__name__) # url_prefix="/auth"
# this auth_bp should connect with app 

## now it is same thing of app.route but this is for authentication

@auth_bp.route("/login", methods=["POST"])
def login():
  print("hello")
  data= request.get_json()

  email= data["email"]
  password= data["password"]

  if (not email or not password):
    return jsonify({"message": "invalid input"}), 400 
  
  ## now if we have email and password ;; we need flask security to very this email and password and this will call **services.py** to get that hashed password which is stored on that email

  user= User.query.filter_by(email= email).first_or_404()

  if user and verify_password(password, user.password):
    # if verify that is user then have to send a token so some infomatin and token(bz it is token base authentication)
    return jsonify({
      "user_id":user.id,
      "username":user.username,
      "email":user.email
    }), 200
  else:
    return jsonify({"message":"There is not any such user!!"}),400