import os
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/")
def home():
    username = os.getenv("USER", "fallbackDaniel")
    return f"Welcome to the Home page {username}!"

if __name__ ==  "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)