
from project.models import db, Login
def authenticate(username,password):

    user  = Login.query.filter_by(username=username,password=password).first()

    return user
def identity(payload):
    user_id = payload["identity"]
    return Login.query.get(user_id)
