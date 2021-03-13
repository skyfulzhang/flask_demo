from marshmallow import fields, Schema, ValidationError, post_load

from users.models import UserModel
from init import db

"""
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(64), index=True, unique=True)
email = db.Column(db.String(120), index=True, unique=True)
password_hash = db.Column(db.String(128))

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


"""
	is_active = db.Column(db.Boolean, default=True, comment="用户是否激活")
	is_super = db.Column(db.Boolean, default=False, comment="用户是否管理员")
	created_at = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

"""


# 序列接口数据为JSON格式
class UserSchema(Schema):
	id = fields.Integer(dump_only=True)
	username = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	email = fields.Email(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	password = fields.String(load_only=True, attribute="password_hash", required=True, validate=validate_null,
	                         error_messages=dict(ErrorMessages))
	is_active = fields.Boolean()
	is_super = fields.Boolean()
	created_at = fields.DateTime(dump_only=True, format="%Y-%m-%d %H:%M:%S")
	updated_at = fields.DateTime(dump_only=True, format="%Y-%m-%d %H:%M:%S")

	@post_load
	def make_author(self, data, **kwargs):
		return UserModel(**data)

	class Meta():
		model = UserModel
		sql_session = db.session


class LoginSchema(Schema):
	email = fields.Email(required=True, validate=validate_null, error_messages=dict(ErrorMessages))
	password = fields.String(required=True, validate=validate_null, error_messages=dict(ErrorMessages))

	class Meta():
		model = None
