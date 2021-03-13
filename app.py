from flask import Flask, request, jsonify
from flask_swagger import swagger

from init import register_db
from init import register_plugins
from init import register_errors
from init import register_blueprint

"""
flask db init  # 初始化操作
flask db migrate # 数据库迁移操作
flask db upgrade # 数据模型升级操作
flask db migrate # 数据库迁移操作
"""


def create_app():
	from config import FlaskConfig
	app = Flask(__name__)
	app.config.from_object(FlaskConfig)
	app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
	with app.app_context():
		register_db(app)
		register_blueprint(app)
		register_plugins(app)
		register_errors(app)

	return app


app = create_app()


@app.route("/spec")
def spec():
	return jsonify(swagger(app))


print(app.url_map)
if __name__ == '__main__':
	app.run(debug=True)
