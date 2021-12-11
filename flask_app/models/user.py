from app import db

class user(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(202), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password
