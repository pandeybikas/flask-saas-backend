from flask_jwt_extended import create_access_token, create_refresh_token
from app.extensions import bycrpt
from app.models.user import Users
from app.api.auth.repository import AuthRepository


class AuthServices:

    @staticmethod
    def register(data:dict):
        email= data.get('email')
        username=data.get('username')
        password=data.get('password_hash')

        #check existing user
        if AuthRepository.get_user_by_email(email):
            raise ValueError("User with this email already exists")
        
        hashed_password=bycrpt.generate_password_hash(password).decode('utf-8')

        user= Users(
            email=email,
            username=username,
            password_hash=hashed_password
        )
        return AuthRepository.create_new_user(user)
    
    @staticmethod
    def login(data:dict):
        email= data.get('email')
        password=data.get('password_hash')

        user= AuthRepository.get_user_by_email(email)
        if not user:
            raise ValueError("Wrong credentials")

        if not bycrpt.check_password_hash(user.password_hash, password):
            raise ValueError("Invalid credentials") 
        
        access_token= create_access_token(identity=user.id)
        refresh_token= create_refresh_token(identity=user.id)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
