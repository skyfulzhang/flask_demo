from flask import Blueprint
from flask_restful import Api

from books.views import BookListCreateAPI, BookRetrieveUpdateDestroyAPI

book = Blueprint('book', __name__)
api = Api(book, prefix="/v1")

# 注册路由
api.add_resource(BookListCreateAPI, '/books')
api.add_resource(BookRetrieveUpdateDestroyAPI, '/books/<int:id>')
