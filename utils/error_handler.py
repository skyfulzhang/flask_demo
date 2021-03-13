from flask import make_response, jsonify
from marshmallow.exceptions import ValidationError


# 注册错误处理
def register_errors(app):
	@app.errorhandler(404)
	def handle_404_error(error):
		return make_response(jsonify({"code": 404, "message": str(error), "data": None}))

	@app.errorhandler(405)
	def handle_405_error(error):
		return make_response(jsonify({"code": 405, "message": str(error), "data": None}))

	@app.errorhandler(ValidationError)
	def handle_valid_error(error):
		return make_response(jsonify({'code': 400, 'message': str(error), "data": None}))
