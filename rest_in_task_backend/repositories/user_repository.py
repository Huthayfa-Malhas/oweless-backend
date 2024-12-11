from rest_in_task_backend.models import User
from rest_in_task_backend.db import db
from werkzeug.security import generate_password_hash

class UserRepository:

    @staticmethod
    def find_by_id(id):
        return db.session.execute(db.select(User).where(User.id == id)).scalar_one_or_none()

    @staticmethod
    def find_by_email(email):
        return db.session.execute(db.select(User).where(User.email == email)).scalar_one_or_none()

    @staticmethod
    def create_user(first_name, last_name, email, password, date_of_birth, gender, commit=True):
        created_user = User(username=f"{first_name}_{last_name}", first_name=first_name, last_name=last_name, email=email, password_hash=generate_password_hash(password), date_of_birth=date_of_birth, gender=gender)
        db.session.add(created_user)
        if commit:
            db.session.commit()
        else:
            db.session.flush()
        
        return created_user
