from flask import Response, request, session
from flask_classful import FlaskView, route
from rest_in_task_backend.components.user_component import UserComponent


class UserView(FlaskView):
    @route('/register', methods=['POST'])
    def register_user(self):
        #TODO validate data
        request_data = request.get_json()
        UserComponent().register_user(request_data)
        response = Response(response="success",
                        status=200,
                        mimetype='application/json')
        return response
 
    @route('/login', methods=['POST'])
    def login_user(self):
        request_data = request.get_json()
        success = UserComponent().login_user(email=request_data['email'], password=request_data['password'])
        response = Response(response="success" if success else "failed",
                        status=200 if success else 401,
                        mimetype='application/json')
        return response

    @route('/logout', methods=['POST'])
    def logout_user(self):
        session.clear()
        return Response(response="success", status=200, mimetype='application/json')
