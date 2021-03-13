from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request, jsonify, make_response

from init import db
from users.models import UserModel
from users.schema import UserSchema
from utils.response import response_200, response_400


class UserListCreateAPI(Resource):
	@jwt_required()
	def get(self):
		# 返回所有数据
		user_list = UserModel.query.all()
		user_data = UserSchema().dump(user_list, many=True)
		res_data = response_200({"users": user_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def post(self):
		try:
			data = request.get_json()
			error = UserSchema().validate(data)
			if error:
				res_data = response_400(msg=str(error))
				return make_response(jsonify(res_data))
			data["password"] = UserModel.generate_password(password=data["password"])
			print(data)
			user = UserSchema().load(data)
			db.session.add(user)
			db.session.commit()
			user_data = UserSchema().dump(user)
			res_data = response_200({"user": user_data})
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))


class UserRetrieveUpdateDestroyAPI(Resource):
	@jwt_required()
	def get(self, id):
		# 返回单条数据
		user = UserModel.query.get(id)
		user_data = UserSchema().dump(user)
		res_data = response_200({"authors": user_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def put(self, id):
		# 修改单条数据
		data = request.get_json()
		UserSchema().validate(data)
		user = UserModel.query.get(id)
		user_json = UserSchema().dump(user)
		for field in user_json:
			if field in data:
				setattr(user, field, data[field])
		db.session.add(user)
		db.session.commit()
		user_data = UserSchema().dump(user)
		res_data = response_200({"authors": user_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def delete(self, id):
		# 删除单条数据
		user = UserModel.query.get(id)
		db.session.delete(user)
		db.session.commit()
		res_data = response_200(data=user.username)
		return make_response(jsonify(res_data))
