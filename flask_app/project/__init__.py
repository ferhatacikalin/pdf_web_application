from flask import Flask
from project.api.routes import api
from project import config
from project.models import db

app = Flask(__name__)

app.register_blueprint(api, url_prefix='/api/v1')
app.config.from_object(config.DevelopmentConfig)
with app.app_context():
    db.init_app(app)
