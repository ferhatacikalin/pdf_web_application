from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    manager_or_user = db.Column(db.BOOLEAN, nullable=False)

    def __init__(self, username, password, manager_or_user):
        self.username = username
        self.password = password
        self.manager_or_user = manager_or_user


class AuthorInfo(db.Model):
    fk_id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, nullable=False)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    student_no = db.Column(db.Integer, nullable=False)
    education_type = db.Column(db.String(60), nullable=False)

    def __init__(self, fk_id, name, surname, student_no, education_type):
        self.fk_id = fk_id
        self.name = name
        self.surname = surname
        self.student_no = student_no
        self.education_type = education_type


class ProjectInfo(db.Model):
    fk_id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, nullable=False)
    lesson_type = db.Column(db.String(80), nullable=False)
    p_title = db.Column(db.String(80), nullable=False)
    p_summary = db.Column(db.Text, nullable=False)
    p_keywords = db.Column(db.Text, nullable=False)
    p_delivery = db.Column(db.String(120), nullable=False)

    def __init__(self, fk_id, lesson_type, p_title, p_summary, p_keywords, p_delivery):
        self.fk_id = fk_id
        self.lesson_type = lesson_type
        self.p_title = p_title
        self.p_summary = p_summary
        self.p_keywords = p_keywords
        self.p_delivery = p_delivery


class AdvisorInfo(db.Model):
    fk_id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, nullable=False)
    advisor_name = db.Column(db.String(80), nullable=False)
    advisor_surname = db.Column(db.String(80), nullable=False)
    advisor_degree = db.Column(db.String(80), nullable=False)

    def __init__(self, fk_id, advisor_name, advisor_surname, advisor_degree):
        self.fk_id = fk_id
        self.advisor_name = advisor_name
        self.advisor_surname = advisor_surname
        self.advisor_degree = advisor_degree


class JuryInfo(db.Model):
    fk_id = db.Column(db.Integer, db.ForeignKey('login.id'), primary_key=True, nullable=False)
    jury_name = db.Column(db.String(90), nullable=False)
    jury_surname = db.Column(db.String(90), nullable=False)
    jury_degree = db.Column(db.String(90), nullable=False)

    def __init__(self, fk_id, jury_name, jury_surname, jury_degree):
        self.fk_id = fk_id
        self.jury_name = jury_name
        self.jury_surname = jury_surname
        self.jury_degree = jury_degree
