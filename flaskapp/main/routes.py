from flask import Blueprint, render_template, request, redirect, url_for
from flaskapp.api.tables import Article, db
import os
import datetime
from flaskapp.config import Config

main = Blueprint('main', __name__)

@main.route('/')
def home_page():
    posts = Article.query.order_by((Article.article_id.desc())).all()
    return render_template('index.html', posts = posts)

@main.route('/post/<int:post_id>')
def post_page(post_id):
    # koruma eklenecek
    post = Article.query.filter(Article.article_id == post_id).first()
    return render_template('post.html', post=post)

#### POSTS ####
@main.route('/betterpython')
def betterpython_page():
    posts = Article.query.filter(Article.category == 'Better Python').order_by((Article.article_id.desc())).all()
    return render_template('posts.html', posts = posts)

@main.route('/blog')
def blog_page():
    posts = Article.query.filter(Article.category == 'Blog').order_by((Article.article_id.desc())).all()
    return render_template('posts.html', posts = posts)

@main.route('/books')
def books_page():
    posts = Article.query.filter(Article.category == 'Books').order_by((Article.article_id.desc())).all()
    return render_template('posts.html', posts = posts)

@main.route('/projects')
def projects_page():
    posts = Article.query.filter(Article.category == 'Projects').order_by((Article.article_id.desc())).all()
    return render_template('posts.html', posts = posts)
