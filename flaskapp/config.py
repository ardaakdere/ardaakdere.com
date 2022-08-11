import os
basedir = os.path.abspath(os.path.dirname(__file__))
print(basedir)

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'sqlite/articles.db')
    SECRET_KEY = "random string"
    IMAGE_UPLOADS = "mysite/static/images/"
    SQLALCHEMY_TRACK_MODIFICATIONS = False