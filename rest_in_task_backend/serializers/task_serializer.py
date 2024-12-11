from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from rest_in_task_backend.models import Task

class TaskSerializer(SQLAlchemySchema):
    class Meta:
        model = Task
        ordered = True

    id = auto_field()
    title = auto_field()
    description = auto_field()
    created_at = auto_field()
    updated_at = auto_field()
