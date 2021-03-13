from flask import request, make_response, jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from datetime import timedelta

from init import db
from users.schema import UserSchema, LoginSchema
from users.models import UserModel
from utils.response import response_200, response_400


class UserLoginResource(Resource):
	"""
	 用户注册接口
    ---
    parameters:
        - in: body
          name: body
          schema:
            required:
                - username
                - password
            properties:
                username:
                    type: string
                    description: 用户名
                    default: ""
                password:
                    type: string
                    description: 用户密码
                    default: ""
	"""

	def post(self):
		try:
			data = request.get_json()
			error = LoginSchema().validate(data)
			if error:
				res_data = response_400(msg=str(error))
				return make_response(jsonify(res_data))
			user = UserModel.query.filter_by(email=data["email"]).first()
			if not user:
				res_data = response_400(msg="user not found")
				return make_response(jsonify(res_data))
			if user.check_password(user.password_hash, data["password"]):
				access_token = create_access_token(identity=data["email"])
				res_data = response_200(data={"token": access_token})
				return make_response(jsonify(res_data))
			else:
				res_data = response_400(msg="email or the password is incorrect")
				return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))
