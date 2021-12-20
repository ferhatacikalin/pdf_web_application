FROM ubuntu:20.04
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -y libmysqlclient-dev
RUN apt install python3.8-venv
WORKDIR /flask_app
RUN pip3 install virtualenv
RUN pip3 install \
    flask\
    flask-cors\
    flask-sqlalchemy\
    mysqlclient\
    Flask-JWT\
    flask-rest-jsonapi\
    jsonify\
    Flask-Reuploaded\
    Werkzeug




CMD [ "python3", "run.py" ]
