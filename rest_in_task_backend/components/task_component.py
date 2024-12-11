from rest_in_task_backend.repositories.task_repository import TaskRepository
from flask import g

class TaskComponent:
    def retrieve_tasks(self, user_id, status=None):
        return TaskRepository.get_all_tasks_by_user_id(user_id=user_id)

    def retrerive_task(self, task_id):
        return TaskRepository.get_by_id(id=task_id)

    def update_task_status(self, task_id, status):
        TaskRepository.update_task_status(task_id=task_id, status=status)

    def create_task(self, title, description, user_id):
        return TaskRepository.create_task(title=title, description=description, user_id=user_id)

    def delete_task(self, task_id):
        TaskRepository.delete_task(task_id=task_id)
