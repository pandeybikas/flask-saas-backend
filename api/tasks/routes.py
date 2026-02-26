from flask import Blueprint

task_bp=Blueprint('/task', __name__)

@task_bp.route('/health')
def health():
    return ({'message': 'health of task is ok!'})
