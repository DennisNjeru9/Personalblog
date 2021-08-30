import os

class Config:
    SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    CSRF_SECRET_KEY = os.environ.get("CSFR_SECRET_KEY")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI= os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog_test'

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI ='postgresql+psycopg2://moringa:Access@localhost/blog'
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}