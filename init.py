from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from marshmallow.exceptions import ValidationError

from utils.response import response_400

db = SQLAlchemy()
cors = CORS()
migrate = Migrate()
marshmallow = Marshmallow()
jwt = JWTManager()


# 初始化数据库
def register_db(app):
	from users.models import UserModel
	from authors.models import AuthorModel
	from books.models import BookModel
	db.init_app(app)
	db.create_all()
	marshmallow.init_app(app)
	migrate.init_app(app, db)


# 注册插件
def register_plugins(app):
	cors.init_app(app, supports_credentials=True)
	jwt.init_app(app)


# 注册蓝图
def register_blueprint(app):
	from users import user
	from authors import author
	from books import book
	app.register_blueprint(user, url_prefix="/api")
	app.register_blueprint(author, url_prefix="/api")
	app.register_blueprint(book, url_prefix="/api")


# 注册错误处理
def register_errors(app):
	@app.errorhandler(404)
	def handle_404_error(error):
		res_data = response_400(msg=str(error))
		return make_response(res_data)

	@app.errorhandler(405)
	def handle_405_error(error):
		res_data = response_400(msg=str(error))
		return make_response(res_data)

	@app.errorhandler(ValidationError)
	def handle_valid_error(error):
		res_data = response_400(msg=str(error))
		return make_response(res_data)
