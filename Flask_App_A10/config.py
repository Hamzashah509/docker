import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(24))
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql+pymysql://ameer:ameer@db/blog_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

