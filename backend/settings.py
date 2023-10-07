import os
import sys

basedir=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

#SQLite URI compatible
WIN=sys.platform.startswith('win')
if WIN:
    prefix='sqlite:///'
else:
    prefix='sqlite:////'

class BaseConfig:
    #APP KEY
    SECRET_KEY=os.getenv('SECRET_KEY','dev key')
    #
    DEBUG_TB_INTERCEPT_REDIRECTS=False
    DEBUG_TB_ENABLED=False
    #SQL ALCHEMY
    SQLALCHEMY_RECORD_QUERIES=True
    #MAIL
    MAIL_SERVER=os.getenv('MAIL_SERVER')
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD=os.getenv('MAIL_PASSWORD')
    MAID_DEFAULT_SENDER=f'BackEnd <{MAIL_USERNAME}>'

    BACKEND_ADMIN_EMAIL=os.getenv('BACKEND_ADMIN_MAIL')

    #QUERT PAGE
    BACKEND_POST_PER_PAGE=10
    BACKEND_MANAGE_POST_PER_PAGE=15
    BACKEND_COMMENT_PER_PAGE=15

    #UPLOAD
    BACKEND_UPLOAD_PATH=os.path.join(basedir,'uploads')
    BACKEND_ALLOWED_IMAGE_EXTENSIONS=['png','jpg','jpeg','gif']

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = prefix + os.path.join(basedir, 'data-dev.db')


class TestingConfig(BaseConfig):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # in-memory database


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data.db'))

config={
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig
    }