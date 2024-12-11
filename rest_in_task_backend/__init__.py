import os

from flask import Flask
from rest_in_task_backend.config import config_dict

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    config_name = os.getenv('FLASK_ENV', 'dev')

    if test_config is None:
        app.config.from_object(config_dict[config_name])
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # TODO config logs

    from .db import db
    # db init
    db.init_app(app)

    # register routes
    _register_routes(app)

    return app

def _register_routes(app):
    from .controllers.task_controller import TasksView
    from .controllers.user_controller import UserView
    TasksView.register(app, trailing_slash=False, route_base='/api/v1/tasks')
    UserView.register(app, trailing_slash=False, route_base='/api/v1/users')
