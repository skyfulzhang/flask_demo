import os, secrets
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.flaskenv'), override=True)


class FlaskConfig(object):
	DEBUG = True
	JSON_AS_ASCII = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///project.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	# JWT_SECRET_KEY = secrets.token_urlsafe(32)
	JWT_SECRET_KEY = "eUwbNgr7XU_WnAyulZVk09vQZ6DJSGiAgcrriVTjmOc"
	JWT_ACCESS_TOKEN_EXPIRES = 3600
	JWT_COOKIE_CSRF_PROTECT = True
	JWT_CSRF_CHECK_FORM = True
	PROPAGATE_EXCEPTIONS = True
