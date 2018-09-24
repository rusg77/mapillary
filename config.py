import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAX_FIELD_LENGTH = 255


class DevelopmentConfig(Config):
    ENV = 'dev'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://mapillary:mapillary@localhost:5432/mapillary'


class DockerConfig(Config):
    ENV = 'dev'
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://mapillary:mapillary@postgres:5432/mapillary'


def get_config():
    if os.environ.get('APP_ENV') == 'docker':
        return DockerConfig
    else:
        return DevelopmentConfig
