from flask import Flask, request, jsonify
from flask_cors import CORS
import json


app = Flask(__name__)
CORS(app)
resources = {r"/api/*": {"origins": "*"}}
app.config["CORS_HEADERS"] = "Content-Type"
app.config['JSON_SORT_KEYS'] = False


@app.route('/')
def home():
    return jsonify({"Message":"Hello world"})

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=8080)
