from rest_in_task_backend.db import db
from rest_in_task_backend.models import Task

class TaskRepository:
    @staticmethod
    def get_by_id(id):
        return db.session.execute(db.select(Task).where(Task.id == id)).scalars().one_or_none()

    @staticmethod
    def get_by_id_and_user_id(id, user_id):
        return db.session.execute(db.select(Task).where(Task.id == id, Task.user_id == user_id)).scalars().one_or_none()

    @staticmethod
    def get_all_tasks_by_user_id(user_id, status=None):
        query = db.select(Task).where(Task.user_id == user_id)
        if status:
            query = query.where(Task.status == status)

        return db.session.execute(query).scalars().all()

    @staticmethod
    def create_task(title, description, user_id, commit=True):
        task = Task(title=title, description=description, user_id=user_id)
        db.session.add(task)
        if commit:
            db.session.commit()
        else:
            db.session.flush()

        return task

    @staticmethod
    def update_task_status(task_id, status, commit=True):
        TaskRepository._update_by_id(task_id, {"status": status}, commit=commit)

    @staticmethod
    def _update_by_id(id, data, commit=True):
        db.session.execute(db.update(Task).where(Task.id == id).values(data))
        if commit:
            db.session.commit()
        else:
            db.session.flush()

    @staticmethod
    def delete_task(task_id, commit=True):
        db.session.execute(db.delete(Task).where(Task.id == task_id))
        if commit:
            db.session.commit()
        else:
            db.session.flush()
