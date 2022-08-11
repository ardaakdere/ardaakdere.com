from flask import Blueprint
from flask_restful import Api

backend = Blueprint('api', __name__)

api = Api(backend)

from flaskapp.api.resources.Articles import Articles

api.add_resource(Articles, '/api/article/<article_id>', '/api/articles')