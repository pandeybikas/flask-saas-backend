from flask import request, Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.api.auth.service import AuthServices


auth_bp=Blueprint('/auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data= request.get_json()
        user= AuthServices.register(data)
        return jsonify({"message": "user registered successfully", "user_id": user.id}), 201
    
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    
@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data= request.get_json()
        tokens= AuthServices.login(data)
        return jsonify(tokens), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 401