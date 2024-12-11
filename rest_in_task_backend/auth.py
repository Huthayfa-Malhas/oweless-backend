from rest_in_task_backend.repositories.task_repository import TaskRepository
from flask import g
from werkzeug.exceptions import Forbidden

class Authorization:
    @staticmethod
    def can_access_task(task_id):
        if not TaskRepository.get_by_id_and_user_id(id=task_id, user_id=g.user.id):
            raise Forbidden()
