from app.extensions import db
from app.models.user import Users

class AuthRepository:
    
    @staticmethod
    def get_user_by_email(email:str):
        return Users.query.filter_by(email=email).first()
    
    @staticmethod
    def create_new_user(user:Users):
        db.session.add(user)
        db.session.commit()
        return user