from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class test(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))

    def __init__(self, body):
        self.body = body

