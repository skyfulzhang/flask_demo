from marshmallow import fields, Schema, post_load, validates, ValidationError, validates_schema

from books.models import BookModel
from init import db

"""
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(64), nullable=False, unique=True, comment="书籍名称")
	desc = db.Column(db.String(128), nullable=False, comment="书籍描述")
	price = db.Column(db.Float, nullable=False, comment="书籍价格")
	publish = db.Column(db.String(64), nullable=False, comment="实际出版社")
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), ondelete='CASCADE')

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
class BookSchema(Schema):
	id = fields.Integer(dump_only=True)
	title = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	price = fields.Float(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	desc = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	publish = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	author_id = fields.Integer(required=True, error_messages={'required': 'author_id is required.'})

	@post_load
	def make_author(self, data, **kwargs):
		return BookModel(**data)

	class Meta():
		model = BookModel
		sql_session = db.session
