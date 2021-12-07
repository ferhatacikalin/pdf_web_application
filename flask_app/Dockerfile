FROM python:3.9-alpine
RUN apk add build-base
WORKDIR /flask_app
RUN python -m pip install --upgrade pip
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
CMD [ "python", "app.py" ]
