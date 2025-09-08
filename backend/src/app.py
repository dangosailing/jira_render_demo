import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGIN", "*")}})

@app.route("/")
def home():
    username = os.getenv("USER", "fallbackDaniel")
    return f"Welcome to the Home page {username}!"

if __name__ ==  "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)