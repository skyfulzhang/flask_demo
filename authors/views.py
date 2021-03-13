from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request, jsonify, make_response

from authors.models import AuthorModel
from authors.schema import AuthorSchema
from utils.response import response_200
from init import db


class AuthorListCreateAPI(Resource):
	@jwt_required()
	def get(self):
		# 返回所有数据
		author_list = AuthorModel.query.all()
		author_data = AuthorSchema().dump(author_list, many=True)
		res_data = response_200({"authors": author_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def post(self):
		# 新增数据
		data = request.get_json()
		author = AuthorSchema().load(data)
		db.session.add(author)
		db.session.commit()
		author_data = AuthorSchema().dump(author)
		res_data = response_200({"author": author_data})
		return make_response(jsonify(res_data))


class AuthorRetrieveUpdateDestroyAPI(Resource):
	@jwt_required()
	def get(self, id):
		# 返回单条数据
		author = AuthorModel.query.get(id)
		author_data = AuthorSchema().dump(author)
		res_data = response_200({"author": author_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def put(self, id):
		# 修改单条数据
		data = request.get_json()
		AuthorSchema().validate(data)
		author = AuthorModel.query.get(id)
		author_json = AuthorSchema().dump(author)
		for field in author_json:
			if field in data:
				setattr(author, field, data[field])
		db.session.add(author)
		db.session.commit()
		author_data = AuthorSchema().dump(author)
		res_data = response_200({"author": author_data})
		return make_response(jsonify(res_data))

	@jwt_required()
	def delete(self, id):
		# 删除单条数据
		author = AuthorModel.query.get(id)
		db.session.delete(author)
		db.session.commit()
		res_data = response_200(data=author.nickname)
		return make_response(jsonify(res_data))
