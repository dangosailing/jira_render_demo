from flask import Blueprint, jsonify

user_bp = Blueprint("user", __name__)

@user_bp.get("/api/user")
def get_user():
    return jsonify({"name": "user"})
