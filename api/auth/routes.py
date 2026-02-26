from flask import request, Blueprint, jsonify

auth_bp=Blueprint('/auth', __name__)


@auth_bp.route('/health')
def health():
    return {'message': 'auth health is ok!'}