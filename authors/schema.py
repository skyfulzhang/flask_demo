from marshmallow import fields, Schema, post_load, validates, ValidationError, validates_schema

from authors.models import AuthorModel
from books.schema import BookSchema
from init import db

"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nickname = db.Column(db.String(16), nullable=False, unique=True, comment="作者昵称")
	age = db.Column(db.Integer, nullable=False, comment="作者年龄")
	native_place = db.Column(db.String(64), nullable=False, comment="作者籍贯")
	books = db.relationship('BookModel', backref='Author', cascade="all, delete-orphan")

"""

ErrorMessages = {
	'required': '该字段必传。',
	'null': '该字段不能为空。',
	'validator_failed': '该字段验证失败。',
	'type': '该字段类型无效。',
	'invalid': '该字段数据类型错误。'
}


def validate_null(data):
	"""一个通用的非空字符串验证器"""
	if not data:
		raise ValidationError("该字段字段不能为空字符串")


# 序列接口数据为JSON格式
class AuthorSchema(Schema):
	id = fields.Integer(dump_only=True)
	nickname = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	age = fields.Integer(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	native_place = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	books = fields.Nested(BookSchema, many=True)

	@post_load
	def make_author(self, data, **kwargs):
		return AuthorModel(**data)

	class Meta():
		model = AuthorModel
		sql_session = db.session
