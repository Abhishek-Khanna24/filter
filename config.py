

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'f9f876f1-0e24-4eca-8ab4-cf0f9682c29e'
    SQLALCHEMY_DATABASE_URI = "postgres://cvwyupld:3Fu0SAYQdkB0f6JWbSpLIn632Y4JQWn9@queenie.db.elephantsql.com:5432/cvwyupld"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True