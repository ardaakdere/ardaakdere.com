from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Article(db.Model):  # type: ignore
    article_id = db.Column(db.Integer, primary_key = True)
    image_name = db.Column(db.String(100), nullable = False)
    title = db.Column(db.String(100), nullable = False)
    category = db.Column(db.String(50), nullable = False)
    content = db.Column(db.String(50), nullable = False)
    author = db.Column(db.String(50), nullable = False)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, image_name, title, category, content, author, date):
        self.image_name = image_name
        self.title = title
        self.category = category
        self.content = content
        self.author = author
        self.date = date