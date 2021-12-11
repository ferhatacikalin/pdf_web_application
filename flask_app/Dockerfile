FROM ubuntu:20.04
RUN apt update
RUN apt install -y python3-pip
RUN apt install -y build-essential libssl-dev libffi-dev python3-dev
RUN apt install -y libmysqlclient-dev
RUN apt install python3.8-venv
WORKDIR /flask_app
RUN python3 -m venv .
RUN bash -c "source bin/activate"
CMD [ "python3", "app.py" ]
