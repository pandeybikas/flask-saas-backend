from datetime import datetime
from app.extensions import db

class Task(db.Model):
    __tablename__='task'

    id= db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(255))
    description= db.Column(db.Text)
    status= db.Column(db.String(200), default='pending')
    user_id= db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at=db.Column(db.DateTime, default=datetime.utcnow)
    updated_at=db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Tasks {self.title}>"