from os import name
from flask import Flask, request, jsonify
import db_models


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"Message":"Hello world"})

if __name__ == "__main__":
    db_models.db.create_all()
    user_one=db_models.deneme(name="berkau",password="53748")
    db_models.db.session.add(user_one)
    db_models.db.session.commit()
    app.run(debug = True, host='0.0.0.0', port=8080)
