from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.common.decorators import role_required

users_bp = Blueprint("users", __name__)


@users_bp.route("/", methods=["GET"])
@jwt_required()
@role_required("admin")
def get_all_users():
    return jsonify({"message": "Only admins can see all users"})