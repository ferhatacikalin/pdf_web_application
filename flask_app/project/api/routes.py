import werkzeug.utils
from flask import Blueprint, jsonify, request, abort, make_response
from flask_jwt import jwt_required, current_identity
from flask_uploads import UploadSet, DOCUMENTS
from project.models import db, Login, AuthorInfo, Documents, ProjectInfo, AdvisorInfo, JuryInfo
from project.getInfo import Advisor, Author, Jury, Project
api = Blueprint('api', __name__)
documents = UploadSet('documents', DOCUMENTS)


@api.route('/me')
@jwt_required()
def me():
    if request.method == "GET":
        return jsonify({
            'id': current_identity.id,
            'username': current_identity.username,
            'is_admin': current_identity.is_admin
        })


@api.route('/user/add', methods=['POST'])
@jwt_required()
def add_user():
    if not current_identity.is_admin:
        return 'unauthorized', 400
    if request.method == "POST":
        user = Login(
            username=request.form.get('username'),
            password=request.form.get("password"),
            is_admin=bool(request.form.get("is_admin") == 'true'),
        )
        db.session.add(user)
        db.session.commit()
        return 'ok', 200


@api.route('/user/list', methods=['GET'])
@jwt_required()
def list_user():
    if not current_identity.is_admin:
        return 'unauthorized', 400
    if request.method == "GET":
        users = Login.query.all()
        list = []
        for user in users:
            list.append({
                'id': user.id,
                'username': user.username,
                'is_admin': user.is_admin

            })

        return jsonify(list)


@api.route('/user/<u_id>', methods=['GET'])
@jwt_required()
def view_user(u_id):
    if not current_identity.is_admin:
        return 'unauthorized', 400
    if request.method == "GET":
        user = Login.query.get(u_id)
        return jsonify({
            'id': user.id,
            'username': user.username,
            'is_admin': user.is_admin
        })


@api.route('/user/update/<u_id>', methods=['POST'])
@jwt_required()
def update_user(u_id):
    if not current_identity.is_admin:
        return 'unauthorized', 400
    username = request.form.get('username')

    is_admin = bool(request.form.get('is_admin') == 'true')

    user = Login.query.get(u_id)
    user.username = username
    user.is_admin = is_admin
    db.session.merge(user)
    db.session.commit()
    return 'ok', 200


@api.route('/user/delete/<u_id>', methods=['GET'])
@jwt_required()
def delete_user(u_id):
    if not current_identity.is_admin:
        return 'unauthorized', 400
    user = Login.query.get(u_id)
    db.session.delete(user)
    db.session.commit()
    return 'ok', 200


@api.route('/query/author/<a_id>', methods=['GET'])
@jwt_required()
def get_author_id(a_id):
    author = AuthorInfo.query.get_or_404(a_id)
    project = ProjectInfo.query.get_or_404(author.id)
    advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
    jury = JuryInfo.query.get_or_404(project.jury_id)

    return jsonify({
        'author_id': author.id,
        'user_id': author.user_id,
        'advisor': {
            'advisor_id': advisor.id,
            'advisor_name': advisor.advisor_name,
            'advisor_surname': advisor.advisor_surname,
            'advisor_degree': advisor.advisor_degree,
        },
        'jury': {
            'jury_id': jury.id,
            'jury_name': jury.jury_name,
            'jury_surname': jury.jury_surname,
            'jury_degree': jury.jury_degree,

        },
        'project': {
            'project_id': project.id,
            'document_id': project.document_id,
            'lesson_type': project.lesseon_type,
            'p_title': project.p_title,
            'p_summary': project.p_summary,
            'p_keywords': project.p_keywords,
            'p_delivery': project.p_delivery

        },
        'name_surname': author.name_surname,
        'student_no': author.student_no,
        'education_type': author.education_type

    });


@api.route('/query/lesson', methods=['POST'])
@jwt_required()
def get_lesson_name():
    list=[]
    projects = ProjectInfo.query.filter(ProjectInfo.lesson_type == request.form['query']).all()
    for project in projects:
            
        author = AuthorInfo.query.get_or_404(project.author_id)
        advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
        jury = JuryInfo.query.get_or_404(project.jury_id)
        list.append({
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

        })

    return jsonify(list);


@api.route('/query/project_name', methods=['POST'])
@jwt_required()
def get_project_name():
    list=[]
    projects = ProjectInfo.query.filter(ProjectInfo.p_title == request.form['query']).all()
    for project in projects:
            
        author = AuthorInfo.query.get_or_404(project.author_id)
        advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
        jury = JuryInfo.query.get_or_404(project.jury_id)
        list.append({
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

        })

    return jsonify(list);

@api.route('/query/delivery', methods=['POST'])
@jwt_required()
def get_project_delivery():
    list=[]
    projects = ProjectInfo.query.filter(ProjectInfo.p_delivery == request.form['query']).all()
    for project in projects:
            
        author = AuthorInfo.query.get_or_404(project.author_id)
        advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
        jury = JuryInfo.query.get_or_404(project.jury_id)
        list.append({
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

        })
        return jsonify(list);

@api.route('/query/keywords', methods=['POST'])
@jwt_required()
def get_project_keywords():
    list=[]
    try:
        projects = ProjectInfo.query.filter(ProjectInfo.p_keywords.like( "%{}%".format(request.form['query']))).all()
        for project in projects:
                
            author = AuthorInfo.query.get_or_404(project.author_id)
            advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
            jury = JuryInfo.query.get_or_404(project.jury_id)
            list.append({
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

            })
            if len(list)==0:
                return jsonify({}),404;

            else:
                return jsonify(list)
    except:
        return 'HATA OLUŞTU',500
@api.route('/query_two', methods=['POST'])
@jwt_required()
def get_query_two():
    
    list=[]
    try:
            projects = ProjectInfo.query.filter(ProjectInfo.p_delivery.like("%{}%".format(request.form['delivery']))).filter(ProjectInfo.user_id== request.form['user_id']).all()
            for project in projects:
                    
                author = AuthorInfo.query.get_or_404(project.author_id)
                advisor = AdvisorInfo.query.get_or_404(project.advisor_id)
                jury = JuryInfo.query.get_or_404(project.jury_id)
                list.append({
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

                })
                if len(list)==0:
                    return jsonify({}),404;

                else:
                    return jsonify(list)
    except:
            return 'HATA OLUŞTU',500


@api.route('/upload_project', methods=['POST'])
@jwt_required()
def upload_project():
    if request.method == 'POST' and 'pdf' in request.files:
        filename = documents.save(request.files['pdf'],
                                  name=werkzeug.utils.secure_filename(request.files['pdf'].filename))
        f = open(documents.path(filename), 'rb')
        
        author=Author(documents.path(filename))
        advisor = Advisor(documents.path(filename))
        jury=Jury(documents.path(filename))
        project_p=Project(documents.path(filename))
        file_to_db = Documents(f.read())
        db.session.add(file_to_db)
        db.session.commit()
        author_info = AuthorInfo(
            user_id=current_identity.id,
            name_surname='  -  '.join(map(str, author.student_name)),
            student_no='  -  '.join(map(str, author.id)),
            education_type='  -  '.join(map(str, author.e_type))
 
        )
        db.session.add(author_info)
        db.session.commit()

        advisor_info = AdvisorInfo(
            user_id=current_identity.id,
            advisor_name='  -  '.join(map(str, advisor.advisor_name)),
            advisor_surname=''.join(map(str, advisor.advisor_name)),
            advisor_degree='  -  '.join(map(str, advisor.advisor_degree))
        )
        db.session.add(advisor_info)
        db.session.commit()

        jury_info = JuryInfo(
            user_id=current_identity.id,
            jury_name='  -  '.join(map(str, jury.jury_name)),
            jury_surname='',
            jury_degree='  -  '.join(map(str, jury.jury_degree))
        )
        db.session.add(jury_info)
        db.session.commit()

        project_info = ProjectInfo(
            user_id=current_identity.id,
            document_id=file_to_db.id,
            author_id=author_info.id,
            advisor_id=advisor_info.id,
            jury_id=jury_info.id,
            lesson_type=' '.join(map(str, project_p.lesson_type)),
            p_title=' '.join(map(str, project_p.project_name)),
            p_summary=' '.join(map(str, project_p.summary)),
            p_keywords=' '.join(map(str, project_p.keyword)),
            p_delivery=' '.join(map(str, project_p.deliveryTime))
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
    if current_identity.is_admin:
        projects = ProjectInfo.query.all()
    else:
        projects = ProjectInfo.query.filter_by(user_id=current_identity.id)
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
