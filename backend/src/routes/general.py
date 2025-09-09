from flask import Blueprint, jsonify

general_bp = Blueprint("general", __name__)

@general_bp.route("/")
def ping():
    return jsonify({"status": "ok"})