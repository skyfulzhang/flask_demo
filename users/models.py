from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from init import db


class UserModel(db.Model):
	"""用户对象"""
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	username = db.Column(db.String(64), index=True, nullable=False, unique=True, comment="用户名称")
	email = db.Column(db.String(120), index=True, nullable=False, unique=True, comment="用户有限")
	password_hash = db.Column(db.String(128), nullable=False, comment="用户哈希密码")
	is_active = db.Column(db.Boolean, default=True, comment="用户是否激活")
	is_super = db.Column(db.Boolean, default=False, comment="用户是否管理员")
	created_at = db.Column(db.DateTime, default=datetime.now, comment="创建时间")
	updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, comment="更新时间")

	@staticmethod
	def generate_password(password):
		"""密码哈希"""
		return generate_password_hash(password)

	@staticmethod
	def check_password(password_hash, password):
		"""检查密码"""
		return check_password_hash(password_hash, password)

	def __str__(self):
		return '<User {}>'.format(self.username)
