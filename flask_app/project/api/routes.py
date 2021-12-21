import werkzeug.utils
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt import jwt_required, current_identity
from flask_uploads import UploadSet, DOCUMENTS
from project.models import db, Login, AuthorInfo, Documents, ProjectInfo, AdvisorInfo, JuryInfo

api = Blueprint('api', __name__)
documents = UploadSet('documents', DOCUMENTS)


@api.route('/me')
@jwt_required()
def me():
    if request.method == "GET":
        return jsonify({
            'id': current_identity.id,
            'username': current_identity.username,
            'is_admin' : current_identity.is_admin
        })


@api.route('/user/add', methods=['POST'])
@jwt_required()
def add_user():
    if request.method == "POST":
        db.create_all()

        user = Login(
            username=request.form.get('username'),
            password=request.form.get("password"),
            is_admin=bool(request.form.get("is_admin") == 'true'),
        )
        db.session.add(user)
        db.session.commit()
        return 'Başarılı'


@api.route('/user/update/<u_id>', methods=['POST'])
@jwt_required()
def update_user(u_id):
    username = request.form.get('username')
    password = request.form.get('password')
    is_admin = bool(request.form.get('is_admin') == 'true')

    user = Login.query.get(u_id)
    user.username = username
    user.password = password
    user.is_admin = is_admin
    db.session.merge(user)
    db.session.commit()
    return 'ok', 200


@api.route('/user/delete/<u_id>', methods=['GET'])
@jwt_required()
def delete_user(u_id):
    user = Login.query.get(u_id)
    db.session.delete(user)
    db.session.commit()
    return 'ok', 200


@api.route('/upload_project', methods=['POST'])
@jwt_required()
def upload_project():
    if request.method == 'POST' and 'pdf' in request.files:
        filename = documents.save(request.files['pdf'],
                                  name=werkzeug.utils.secure_filename(request.files['pdf'].filename))
        f = open(documents.path(filename), 'rb')
        file_to_db = Documents(f.read())
        db.session.add(file_to_db)
        db.session.commit()
        author_info = AuthorInfo(
            user_id=current_identity.id,
            name_surname="test author",
            student_no=1234,
            education_type='ikinic öğretim'

        )
        db.session.add(author_info)
        db.session.commit()

        advisor_info = AdvisorInfo(
            user_id=current_identity.id,
            advisor_name="advisor test",
            advisor_surname="surname",
            advisor_degree="iyi bir derece"
        )
        db.session.add(advisor_info)
        db.session.commit()

        jury_info = JuryInfo(
            user_id=current_identity.id,
            jury_name="juri test",
            jury_surname="juri surname",
            jury_degree="iyi bir derece"
        )
        db.session.add(jury_info)
        db.session.commit()

        project_info = ProjectInfo(
            user_id=current_identity.id,
            document_id=file_to_db.id,
            author_id=author_info.id,
            advisor_id=advisor_info.id,
            jury_id=jury_info.id,
            lesson_type="lesson type test",
            p_title="title test",
            p_summary="summary summary",
            p_keywords="asd,bsd,bsd",
            p_delivery="p delivery"
        )
        db.session.add(project_info)
        db.session.commit()
        return str(project_info.id), 200
    else:
        abort(400)


@api.route('/project/<p_id>', methods=['GET'])
@jwt_required()
def view_project(p_id):
    project = ProjectInfo.query.get_or_404(p_id)
    author = AuthorInfo.query.get_or_404(project.author_id)
    advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
    jury = JuryInfo.query.get_or_404(project.jury_id)
    return jsonify({
        'project_id': project.id,
        'user_id': project.user_id,
        'document_id': project.document_id,
        'author': {
            'id': author.id,
            'name_surname': author.name_surname,
            'student_no': author.student_no,
            'education_type': author.education_type
        },
        'advisor': {
            'advisor_name': advisor.advisor_name,
            'advisor_surname': advisor.advisor_surname,
            'advisor_degree': advisor.advisor_degree,
        },
        'jury': {
            'jury_name': jury.jury_name,
            'jury_surname': jury.jury_surname,
            'jury_degree': jury.jury_degree

        },
        'lesson_type': project.lesson_type,
        'p_title': project.p_title,
        'p_summary': project.p_summary,
        'p_keywords': project.p_keywords,
        'p_delivery': project.p_delivery

    });


@api.route('/project/list', methods=['GET'])
@jwt_required()
def list_project():
    projects = ProjectInfo.query.all()
    list = []
    for project in projects:
        author = AuthorInfo.query.get_or_404(project.author_id)
        advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
        jury = JuryInfo.query.get_or_404(project.jury_id)
        item = {
            'project_id': project.id,
            'user_id': project.user_id,
            'document_id': project.document_id,
            'author': {
                'id': author.id,
                'name_surname': author.name_surname,
                'student_no': author.student_no,
                'education_type': author.education_type
            },
            'advisor': {
                'advisor_name': advisor.advisor_name,
                'advisor_surname': advisor.advisor_surname,
                'advisor_degree': advisor.advisor_degree,
            },
            'jury': {
                'jury_name': jury.jury_name,
                'jury_surname': jury.jury_surname,
                'jury_degree': jury.jury_degree

            },
            'lesson_type': project.lesson_type,
            'p_title': project.p_title,
            'p_summary': project.p_summary,
            'p_keywords': project.p_keywords,
            'p_delivery': project.p_delivery

        }
        list.append(item)


    return jsonify(list);


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
