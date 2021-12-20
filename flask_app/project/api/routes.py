import werkzeug.utils
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt import jwt_required, current_identity
from flask_uploads import UploadSet, DOCUMENTS

from project.models import db, Login, AuthorInfo, Documents

api = Blueprint('api', __name__)
documents = UploadSet('documents', DOCUMENTS)


@api.route('/me')
@jwt_required()
def me():
    if request.method == "GET":
        # return user
        return jsonify({
            'id': current_identity.id,
            'username': current_identity.username
        })


@api.route('/user/add', methods=['GET','POST'])
def add_user():
    if request.method == "POST":
        db.create_all()
        user = Login(
            username=request.form.get('username'),
            password=request.form.get("password"),
            is_admin=request.form.get("is_admin"),
        )
        db.session.add(user)
        db.session.commit()
        return 'Başarılı'

@api.route('/user/update',methods=['GET','POST'])
def update_user():
    username=request.form.get('username')
    old_pass=request.form.get('old-password')
    new_pass=request.form.get('new-password')
    user = Login.query().filter(Login.username==username and Login.password==old_pass)
    user['password']=new_pass
    db.session.merge(user)
    db.session.commit()
    
    
    
    

@api.route('/upload_project', methods=['POST'])
# @jwt_required()
def upload_project():
    if request.method == 'POST' and 'pdf' in request.files:
        filename = documents.save(request.files['pdf'],
                                  name=werkzeug.utils.secure_filename(request.files['pdf'].filename))
        f = open(documents.path(filename), 'rb')
        file_to_db = Documents(None, f.read())
        db.session.add(file_to_db)
        db.session.commit()
        return 'ok'
    else:
        abort(400)


@api.route('/download_document/<id>')
def download_document(id):
    download = Documents.query.get_or_404(id)
    response = make_response(download.document)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set(
        'Content-Disposition', 'attachment', filename='document.pdf')
    return response


@api.route('/view')
def view():
    return documents.url('1.pdf')


@api.route('/db')
def db_test():
    db.create_all()
    userone = Login("Ferhat", "Ferhat", True)
    usertwo = Login("Berkay", "Berkay", False)
    db.session.add(userone), db.session.add(usertwo)
    db.session.commit()
    return 'Kullanıcı eklendi'


@api.route('/dbdelete')
def delete_database_data():
    db.session.query(AuthorInfo).delete()
    db.session.query(Login).delete()
    db.session.commit()
    return "Silme İşlemi Gerçekleşti"
