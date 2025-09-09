import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from src.routes.general import general_bp
from src.routes.user import user_bp

load_dotenv()

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": os.getenv("CORS_ORIGIN", "*")}})

app.register_blueprint(general_bp)
app.register_blueprint(user_bp)

if __name__ ==  "__main__":
        app.run(host="0.0.0.0", port=5000, debug=True)