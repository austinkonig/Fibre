from flask import Blueprint, request, jsonify
from app.models.user import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    user = User().find_user_by_email(email)
    if user:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "User not found"}), 404
