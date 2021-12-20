from flask import Flask
from flask_uploads import UploadSet, DOCUMENTS, configure_uploads

from project.api.routes import api
from project import config
from project.models import db
from flask_jwt import JWT
from project.auth import authenticate, identity
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
jwt= JWT(app,authenticate,identity)
document = UploadSet('documents', DOCUMENTS)

app.config.from_object(config.DevelopmentConfig)
configure_uploads(app, document)

app.register_blueprint(api, url_prefix='/api/v1')
with app.app_context():
    db.init_app(app)
