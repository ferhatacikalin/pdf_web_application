import os
import datetime
class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://localhost:87654321@mysql/pdf_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "asdasdasdasdasdasdasdssassa"
    JWT_AUTH_HEADER_PREFIX = "Bearer"
    JWT_ACCESS_TOKEN_EXPIRES =0
    JWT_VERIFY_CLAIMS = ['signature', 'nbf', 'iat']
    JWT_REQUIRED_CLAIMS = []
    UPLOADED_DOCUMENTS_DEST = "static/documents"
    SECRET_KEY = 'os.urandom(24)'
    JWT_EXPIRATION_DELTA = datetime.timedelta(seconds=3000000000)
class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True


class TestingConfig:
    DEBUG = False
    TESTING = True
