from init import db


# 作者模型
class AuthorModel(db.Model):
	__tablename__ = 'authors'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	nickname = db.Column(db.String(16), nullable=False, unique=True, comment="作者昵称")
	age = db.Column(db.Integer, nullable=False, comment="作者年龄")
	native_place = db.Column(db.String(64), nullable=False, comment="作者籍贯")
	books = db.relationship('BookModel', backref='Author', cascade="all, delete-orphan")

	def __repr__(self):
		return '<Author %s>' % self.nickname


"""
封装Author的CRUD
"""
