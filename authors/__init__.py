from flask import Blueprint
from flask_restful import Api

from authors.views import AuthorListCreateAPI, AuthorRetrieveUpdateDestroyAPI

author = Blueprint('authors', __name__)
api = Api(author, prefix="/v1")

# 注册路由
api.add_resource(AuthorListCreateAPI, '/authors')
api.add_resource(AuthorRetrieveUpdateDestroyAPI, '/authors/<int:id>')
