from flask_jwt_extended import jwt_required
from flask_restful import Resource
from flask import request, jsonify, make_response

from init import db
from books.models import BookModel
from books.schema import BookSchema
from utils.response import response_200, response_400


class BookListCreateAPI(Resource):
	@jwt_required()
	def get(self):
		# 返回所有数据
		try:
			book_list = BookModel.query.all()
			book_data = BookSchema().dump(book_list, many=True)
			res_data = response_200({"books": book_data})
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))

	@jwt_required()
	def post(self):
		# 新增数据
		data = request.get_json()
		error = BookSchema().validate(data)
		if error:
			res_data = response_400(msg=str(error))
			return make_response(jsonify(res_data))
		try:
			book = BookSchema().load(data)
			db.session.add(book)
			db.session.commit()
			book_data = BookSchema().dump(book)
			res_data = response_200({"book": book_data})
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))


class BookRetrieveUpdateDestroyAPI(Resource):
	@jwt_required()
	def get(self, id):
		# 返回单条数据
		try:
			book = BookModel.query.get(id)
			if not book:
				res_data = response_400(msg="book not found")
				return make_response(jsonify(res_data))
			book_data = BookSchema().dump(book)
			res_data = response_200({"authors": book_data})
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))

	@jwt_required()
	def put(self, id):
		# 修改单条数据
		data = request.get_json()
		error = BookSchema().validate(data)
		if error:
			res_data = response_400(msg=str(error))
			return make_response(jsonify(res_data))
		try:
			book = BookModel.query.get(id)
			if not book:
				res_data = response_400(msg="book not found")
				return make_response(jsonify(res_data))
			book_json = BookSchema().dump(book)
			for field in book_json:
				if field in data:
					setattr(book, field, data[field])
			db.session.add(book)
			db.session.commit()
			book_data = BookSchema().dump(book)
			res_data = response_200({"authors": book_data})
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))

	@jwt_required()
	def delete(self, id):
		# 删除单条数据
		try:
			book = BookModel.query.get(id)
			if not book:
				res_data = response_400(msg="book not found")
				return make_response(jsonify(res_data))
			db.session.delete(book)
			db.session.commit()
			res_data = response_200(data=book.title)
			return make_response(jsonify(res_data))
		except Exception as e:
			res_data = response_400(msg=str(e))
			return make_response(jsonify(res_data))
