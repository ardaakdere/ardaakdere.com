from flask_restful import Resource, reqparse
from flaskapp.api.tables import db, Article

class Articles(Resource):
    
    def __init__(self) -> None:
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('article_id', type=int)
    
    def get(self, article_id = None):
        
        if not article_id:
            result = {}
            articles = Article.query.order_by((Article.article_id.desc())).all()
            for article in articles:
                result[article.article_id] = {
                    'title': article.title,
                    'image_name': article.image_name,
                    'category': article.category,
                    'author': article.author,
                    'date': article.date.strftime('%Y-%m-%d'),
                    'content': article.content
                }
            return result
        else:
            article = Article.query.filter(Article.article_id == article_id).first()

            if not article:
                return "None"
            else:
                result = {
                    article.article_id: {
                        'title': article.title,
                        'image_name': article.image_name,
                        'category': article.category,
                        'author': article.author,
                        'date': article.date.strftime('%Y-%m-%d'),
                        'content': article.content
                    }
                }
                return result
