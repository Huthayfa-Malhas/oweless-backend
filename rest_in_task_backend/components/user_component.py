from flask import session
from rest_in_task_backend.repositories.user_repository import UserRepository
from werkzeug.security import check_password_hash

class UserComponent:

    def register_user(self, request_data):
        _ = UserRepository.create_user(first_name=request_data["first_name"], last_name=request_data["last_name"], email=request_data["email"], password=request_data["password"], date_of_birth=request_data['date_of_birth'], gender=request_data['gender'])

    def login_user(self, email, password):
        user = UserRepository.find_by_email(email=email)
        if user and user.check_password(password_hash=user.password_hash, password=password):
            session.clear()
            #TODO store in DB for distributed systems
            session['user_id'] = user.id
            return True

        return False
