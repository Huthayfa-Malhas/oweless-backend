from flask import Response, request
import json
from flask_classful import FlaskView
from rest_in_task_backend.components.task_component import TaskComponent
from rest_in_task_backend.serializers.task_serializer import TaskSerializer
from flask import session, g
from rest_in_task_backend.decorators import login_required
from rest_in_task_backend.repositories.user_repository import UserRepository
from rest_in_task_backend.auth import Authorization

class TasksView(FlaskView):
    decorators = [login_required]

    #TODO create base view class
    def before_request(self, name, *args, **kwargs):
        # load user into g
        user_id = session.get('user_id')

        if user_id is None:
            g.user = None
        else:
            g.user = UserRepository.find_by_id(user_id)


    # GET api/v1/tasks
    def index(self):
        data = TaskComponent().retrieve_tasks(user_id=g.user.id)
        serialzied_data = TaskSerializer(only=["id", "title", "description", "created_at", "updated_at"]).dump(data, many=True)
        
        response = Response(response=json.dumps(serialzied_data),
                        status=200,
                        mimetype='application/json')
        return response
        


    # GET api/v1/tasks/<id>
    def get(self, id):
        Authorization.can_access_task(id)

        data = TaskComponent().retrerive_task(task_id=id)
        serialzied_data = TaskSerializer(only=["id", "title", "description", "created_at", "updated_at"]).dump(data)
        
        response = Response(response=json.dumps(serialzied_data),
                        status=200,
                        mimetype='application/json')
        return response

    # PUT api/v1/tasks/<id>
    def update(self, id):
        #TODO validate data
        Authorization.can_access_task(id)

        TaskComponent().update_task_status(task_id=id, status=request.get_json()['status'])
        return Response(response="success", status=200, mimetype='application/json')

    # POST api/v1/tasks
    def post(self):
        #TODO validate data
        request_data = request.get_json()
        created_task = TaskComponent().create_task(title=request_data['title'], description=request_data['description'], user_id=g.user.id)
        return Response(response=json.dumps({"id": created_task.id}),
                        status=201,
                        mimetype='application/json')

    # DELETE api/v1/tasks/<id>
    def delete(self, id):
        Authorization.can_access_task(id)

        TaskComponent().delete_task(task_id=id)
        return Response(response="success", status=200, mimetype='application/json')
