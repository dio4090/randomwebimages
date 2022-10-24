import os
from datetime import timedelta
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Mudar a SECRET_KET em producção
    SECRET_KEY = os.environ.get("SECRET_KEY", os.urandom(24))
    DEBUG = False

    # JWT configuraçãp
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", os.urandom(24))
    ## Tempo de expiração do token
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data-dev.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "sqlite:///" + os.path.join(basedir, "data.sqlite")
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig,
    default=DevelopmentConfig,
)

load_dotenv()

BRANCH_NAME = os.environ.get('BRANCH_NAME')
APP_PORT = os.environ.get('PORT', 5000)

BC_API_KEY = os.getenv('BC_API_KEY')
BC_DOMAIN = os.getenv('BC_DOMAIN')
