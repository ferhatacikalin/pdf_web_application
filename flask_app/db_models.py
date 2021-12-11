from app import db

class deneme(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password
