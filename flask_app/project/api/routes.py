from flask import Blueprint

api = Blueprint('api', __name__)

@api.route('/me')
def index():
	return "Hello, World! This is the api page."