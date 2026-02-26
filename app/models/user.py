from datetime import datetime
from app.extensions import db


class Users(db.Model):
    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(180), unique=True)
    password_hash= db.Column(db.String(255))
    role= db.Column(db.String(50))
    is_active= db.Column(db.Boolean, default=True)
    created_at= db.Column(db.DateTime, default=datetime.utcnow)
    updated_at= db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    tasks= db.relationship("Task", backref="owner", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"