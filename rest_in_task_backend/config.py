import os
from sqlalchemy import URL
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = URL.create(
        "postgresql",
        username=os.environ['DATABASE_USERNAME'],
        password=os.environ['DATABASE_PASSWORD'],
        host=os.environ['DATABASE_HOST'],
        database=os.environ['DATABASE_NAME'],
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass


config_dict = {
    "dev": DevelopmentConfig,
    "test": TestingConfig,
    "prod": ProductionConfig
}