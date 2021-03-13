from flask import Blueprint
from flask_restful import Api

from users.views import UserListCreateAPI, UserRetrieveUpdateDestroyAPI
from users.security import UserLoginResource

user = Blueprint('user', __name__)
api = Api(user, prefix="/v1")

# 注册路由
api.add_resource(UserListCreateAPI, '/users')
api.add_resource(UserRetrieveUpdateDestroyAPI, '/users/<int:id>')
api.add_resource(UserLoginResource, '/user/login')
