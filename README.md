Setup Instructions
1. Clone Repository

git clone https://github.com/your-username/flask-saas-backend.git

cd flask-saas-backend

2. Create Virtual Environment

python -m venv envv

Activate:

Windows:
envv\Scripts\activate

Mac/Linux:
source envv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

Environment Variables

Create a .env file in the root directory:

FLASK_ENV=development
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret

DB_USER=root
DB_PASSWORD=yourpassword
DB_HOST=localhost
DB_NAME=flask_saas

Database Setup

Create database in MySQL:

CREATE DATABASE flask_saas;

Run migrations:

flask db migrate -m "Initial migration"
flask db upgrade

Available Endpoints

Auth:

POST /api/v1/auth/register

POST /api/v1/auth/login
A production-ready Flask backend built using clean architecture principles.
This project demonstrates scalable backend structure, authentication, authorization, and database management using industry-standard practices.
Architecture

The project follows a layered architecture:

Route → Service → Repository → Model → Database
Tech Stack

Python

Flask (App Factory Pattern)

Flask-SQLAlchemy

Flask-Migrate

Flask-JWT-Extended

Flask-Bcrypt

MySQL

Marshmallow

Pytest
