from flask import Blueprint
from project.models import db, Login, AuthorInfo

api = Blueprint('api', __name__)


@api.route('/me')
def index():
    return "Hello, World! This is the api page."


@api.route('/db')
def db_test():
    db.create_all()
    userone = Login("Ferhat", "Ferhat", True)
    usertwo = Login("Berkay", "Berkay", False)
    db.session.add(userone), db.session.add(usertwo)
    db.session.commit()
    authorone = AuthorInfo(1, "Kerem", "Demir", "180495321", "İkinci Öğretim")
    authortwo = AuthorInfo(2, "Demir", "Er", "190741854", "Birinci Öğretim")
    db.session.add(authorone), db.session.add(authortwo)
    db.session.commit()
    return " Yazar Ekleme  Başarılı"


@api.route('/dbdelete')
def delete_database_data():
    db.session.query(AuthorInfo).delete()
    db.session.query(Login).delete()
    db.session.commit()
    return "Silme İşlemi Gerçekleşti"
