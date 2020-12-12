import os

SECRET_KEY = 'top-secret'
# SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite')
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'mysql://root:password@localhost/subscription')
SQLALCHEMY_TRACK_MODIFICATIONS = False
