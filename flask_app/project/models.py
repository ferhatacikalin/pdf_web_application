from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.BOOLEAN, nullable=False)

    def __init__(self, username, password, is_admin):
        self.username = username
        self.password = password
        self.is_admin = is_admin


class AuthorInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    name_surname = db.Column(db.String(80), nullable=False)
    student_no = db.Column(db.String(80), nullable=False)
    education_type = db.Column(db.String(60), nullable=False)

    def __init__(self, user_id, name_surname, student_no, education_type):
        self.user_id = user_id
        self.name_surname = name_surname
        self.student_no = student_no
        self.education_type = education_type


class ProjectInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    document_id = db.Column(db.Integer, db.ForeignKey('documents.id'), nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author_info.id'), nullable=False)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor_info.id'), nullable=False)
    jury_id = db.Column(db.Integer, db.ForeignKey('jury_info.id'), nullable=False)
    lesson_type = db.Column(db.String(80), nullable=False)
    p_title = db.Column(db.String(80), nullable=False)
    p_summary = db.Column(db.Text, nullable=False)
    p_keywords = db.Column(db.Text, nullable=False)
    p_delivery = db.Column(db.String(120), nullable=False)

    def __init__(self, user_id, document_id, author_id, advisor_id, jury_id,
                 lesson_type, p_title, p_summary, p_keywords, p_delivery):
        self.user_id = user_id
        self.document_id = document_id
        self.author_id = author_id
        self.advisor_id = advisor_id
        self.jury_id = jury_id
        self.lesson_type = lesson_type
        self.p_title = p_title
        self.p_summary = p_summary
        self.p_keywords = p_keywords
        self.p_delivery = p_delivery


class AdvisorInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    advisor_name = db.Column(db.String(80), nullable=False)
    advisor_surname = db.Column(db.String(80), nullable=False)
    advisor_degree = db.Column(db.String(80), nullable=False)

    def __init__(self, user_id, advisor_name, advisor_surname, advisor_degree):
        self.user_id = user_id

        self.advisor_name = advisor_name
        self.advisor_surname = advisor_surname
        self.advisor_degree = advisor_degree


class JuryInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_id = db.Column(db.Integer,  nullable=False)
    jury_name = db.Column(db.String(90), nullable=False)
    jury_surname = db.Column(db.String(90), nullable=False)
    jury_degree = db.Column(db.String(90), nullable=False)

    def __init__(self, user_id, jury_name, jury_surname, jury_degree):
        self.user_id = user_id

        self.jury_name = jury_name
        self.jury_surname = jury_surname
        self.jury_degree = jury_degree


class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document = db.Column(db.LargeBinary(length=(2 ** 32) - 1))

    def __init__(self, document):
        self.document = document
