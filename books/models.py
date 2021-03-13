from init import db


# 书籍模型
class BookModel(db.Model):
	__tablename__ = 'books'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(64), nullable=False, unique=True, comment="书籍名称")
	desc = db.Column(db.String(128), nullable=False, comment="书籍描述")
	price = db.Column(db.Float, nullable=False, comment="书籍价格")
	publish = db.Column(db.String(64), nullable=False, comment="实际出版社")
	author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

	def __repr__(self):
		return '<Book %s>' % self.title
